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
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(0.5)
            createFile(driver)
            driver.switch_to.window(main)
    return

def createFile(driver):
    wait = WebDriverWait(driver, 10)
    job = createJob()
    try:
        title = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'dashboard-header__profile-information-name')))
        #print(title, title[0].text)
        job['title'] = title[0].text
    except Exception as e:
        print(str(e))

    # try:
    #     elements = driver.find_element((By.TAG_NAME, 'tr'))
    #     for elem in elements:
    #         try:
    #             if elem.find_element((By.TAG_NAME, 'strong'))[0].text == 'Job Description:':

    #         except Exception as e:
    #             print(str(e))
        
    # except Exception as e:
    #     print(str(e))
    
    
    
    current = os.getcwd()
    if not os.path.exists(current):
        os.makedirs(current)
    filepath = os.path.join(current, title[0].text)
    try:
        f = open(filepath, "w")
        f.write(json.dumps(job))
        f.close()
    except Exception as e:
        print(str(e))


    driver.close()
    return 

def createJob():
    result = {}
    result['description'] = 'None'
    result['title'] = 'None'
    result['organization'] = 'None'
    result['address'] = 'None'
    result['city'] = 'None'
    result['province'] = 'None'
    result['postal'] = 'None'
    return result

    