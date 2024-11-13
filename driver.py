import sys
import time
from login import login
from scraper import createFile
from createCoverLetter import createCoverLetter
from upload import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(args):
    user = args[1]
    secret = args[2]
    driver = login(user, secret)

    if driver == None:
        print("Sanity check login failed")
        return
    
    
    
    main = driver.window_handles[0]

    # wait = WebDriverWait(driver, 10)
    # bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))
    # for btn in bottons:
    #     if btn.text == 'Apply':
            
    #         btn.click()
    #         driver.switch_to.window(driver.window_handles[1])
    #         time.sleep(0.5)
    #         title = createFile(driver)
    #         createCoverLetter(title, "Cover_letter_test.docx") # second argument should be decided by selector TO DO
    #         driver.switch_to.window(main)
    #         break
    

    driver.switch_to.window(driver.window_handles[-1])
    upload_cover_letter(driver, 'test.pdf')
    
    time.sleep(10)
    driver.quit()

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("need 3 args")
    else:
        main(sys.argv)