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
    wait = WebDriverWait(driver, 10)
    try:
        btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'applyButton')))
        btn.click()
        
    except Exception as e:
        print('apply button error\n' ,str(e))

    try:
        radio = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input[type='radio'][value='customPkg']")))
        radio.click()
        
    except Exception as e:
        print('radio error\n' ,str(e))

    title_elem = driver.find_element(By.ID, 'packageName')
    title_elem.send_keys(title)

    SIS = Select(driver.find_element(By.ID, 'requiredPackage18'))
    SIS.select_by_index(1)

    cover = Select(driver.find_element(By.ID, 'requiredPackage14'))
    cover.select_by_index(1)

    resume = Select(driver.find_element(By.ID, 'requiredPackage15'))
    resume.select_by_index(1)

    transcript = Select(driver.find_element(By.ID, 'requiredPackage16'))
    transcript.select_by_index(1)

    submit = driver.find_element(By.CSS_SELECTOR, "input[type='Submit']")




    