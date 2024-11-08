import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import json

def scraper(driver):
    
    main= driver.window_handles[0]

    wait = WebDriverWait(driver, 10)
    bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))
    for btn in bottons:
        if btn.text == 'Apply':
            
            btn.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(0.5)
            createFile(driver)
            driver.switch_to.window(main)
    return

def createFile(driver):
    wait = WebDriverWait(driver, 10)
    try:
        title = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'dashboard-header__profile-information-name')))
        #print(title, title[0].text)
    except Exception as e:
        print('title error\n' ,str(e))
    
    
    print('Creating file for job', title[0].text)
    current = os.getcwd()
    if not os.path.exists(current):
        os.makedirs(current)
    filepath = os.path.join(current, 'Jobs', title[0].text)
    try:
        f = open(filepath, "w")
        
        try:
            elements = driver.find_elements(By.TAG_NAME, 'tr')
            print('how many elements walking through:', len(elements))
            for elem in elements:
                f.write(elem.text + '#\n')
            
        except Exception as e:
            print('tr error\n',str(e))
        
        f.close()
    except Exception as e:
        print('file Error',str(e))


    driver.close()
    return 


    