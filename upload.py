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

def upload(driver):
    wait = WebDriverWait(driver, 10)
    try:
        name = wait.until(EC.presence_of_all_elements_located((By.ID,'docName')))
        name.send_keys('Cover_Letter')

    except Exception as e:
        print('Name error\n' ,str(e))
        