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

def applier(driver, title):

    # on correct page click apply
    wait = WebDriverWait(driver, 120)
    try:
        btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'applyButton')))
        btn.click()
     
    except Exception as e:
        print('apply button error\n' ,str(e))

    # click button that to make new package
    try:
        radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='radio'][value='customPkg']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", radio)
        radio.click()
        
    except Exception as e:
        print('radio error\n' ,str(e))

    try:
        # name the package the job title and use all most recent posts
        title_elem = driver.find_element(By.ID, 'packageName')
        title_elem.send_keys(title)

        SIS = Select(driver.find_element(By.ID, 'requiredInPackage18'))
        SIS.select_by_index(1)

        cover = Select(driver.find_element(By.ID, 'requiredInPackage14'))
        cover.select_by_index(1)

        resume = Select(driver.find_element(By.ID, 'requiredInPackage15'))
        resume.select_by_index(1)

        transcript = Select(driver.find_element(By.ID, 'requiredInPackage16'))
        transcript.select_by_index(1)

        # sumbit the job
        submit = driver.find_element(By.CSS_SELECTOR, "input[type='Submit']")
        submit.click()
    
    except Exception as e:
        print('select or submit error\n' ,str(e))

    