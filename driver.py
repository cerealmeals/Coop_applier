import sys
import time
from login import login
from scraper import scraper
from createCoverLetter import createCoverLetter
from applier import applier
from selector import selector
from upload import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os


def main(user, secret, search):

    # sanity checks 
    current = os.path.dirname(os.path.abspath(__file__))
    cover_prio = os.path.join(current, 'cover_letters', 'priority')
    if not os.path.exists(cover_prio):
        print('Error: The cover letter priority file doesn\'t exist. You have either not added a cover letter or the priority file is corrupted or deleted')
        return
    cover_dr = os.path.join(current, 'cover_letters')
    if len(os.listdir(cover_dr)) <= 1:
        print('Error: No cover letters. You have either not added a cover letter or the cover letter is corrupted or deleted')
        return
    resume_prio = os.path.join(current, 'resumes', 'priority')
    if not os.path.exists(resume_prio):
        print('Error: The resume priority file doesn\'t exist. You have either not added a resume or the priority file for the cover letter is corrupted or deleted')
        return
    resume_dr = os.path.join(current, 'resumes')
    if len(os.listdir(resume_dr)) <= 1:
        print('Error: No resumes. You have either not added a resume or the resume is corrupted or deleted')
        return
    
    driver = login(user, secret, search)
    if driver == None:
        print("Error: login failed")
        return
    
    
    
    # main loop
    main = driver.window_handles[0]
    wait = WebDriverWait(driver, 60)
    bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))

    for btn in bottons:
        if btn.text == 'Apply':
            
            btn.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(0.5)
            title = scraper(driver)
            
            if title != "NONE":
                driver.switch_to.window(driver.window_handles[-1])
                cover_letter, resume = selector(title)
                flag = createCoverLetter(title, cover_letter)
                upload_cover_letter(driver, title + '.pdf')
                upload_resume(driver, resume)

                #print('Apply online?', flag)
                if flag:
                    todo = os.path.join(current, 'TODO', title)
                    cover_path = os.path.join(cover_dr, title + '.pdf')
                    resume_path = os.path.join(resume_dr, resume)
                    shutil.copy2(cover_path, todo)
                    shutil.copy2(resume_path, todo)

                driver.switch_to.window(driver.window_handles[1])
                applier(driver, title)
                driver.close()
                driver.switch_to.window(main)
                
                # delete created cover letters
                
                if os.path.exists(os.path.join(cover_dr, title + '.docx')):
                    
                    os.remove(os.path.join(cover_dr, title + '.docx'))
                
                if os.path.exists(os.path.join(cover_dr, title + '.pdf')):
                    os.remove(os.path.join(cover_dr, title + '.pdf'))
            else:
                driver.switch_to.window(main)

            
    
    time.sleep(20)
    driver.quit()

