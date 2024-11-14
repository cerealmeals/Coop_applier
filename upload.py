from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import os
import time

cover_letters = os.path.dirname(os.path.abspath(__file__))

resumes = os.path.join(cover_letters, 'resumes')
cover_letters = os.path.join(cover_letters, 'cover_letters')



def upload_cover_letter(driver, file):
    
    wait = WebDriverWait(driver, 10)
    try:
        name = wait.until(EC.presence_of_element_located((By.ID,'docName')))
        name.send_keys('Cover_Letter')

    except Exception as e:
        print('Name error\n' ,str(e))
    
    try:
        select = Select(wait.until(EC.presence_of_element_located((By.ID, "docType"))))
        select.select_by_visible_text('Cover Letter - .pdf, .doc or .docx')
    except TimeoutException as ex:
        print("Error doc type", str(ex))
    except Exception as e:
        print(str(e))


    submit = driver.find_element(By.ID, 'submitFileUploadFormBtn')

    file_elem = driver.find_element(By.ID, 'fileUpload_docUpload')
    file_elem.send_keys(os.path.join(cover_letters, file))

    wait_for_disable(submit)
    wait_for_enable(submit)
    
    submit.click()

    bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))
    for btn in bottons:
        if btn.text == 'Upload Document':
            btn.click()
            break
    return

def upload_resume(driver, file):

    wait = WebDriverWait(driver, 10)
    try:
        name = wait.until(EC.presence_of_element_located((By.ID,'docName')))
        name.send_keys('resume')

    except Exception as e:
        print('Name error\n' ,str(e))
    
    try:
        select = Select(wait.until(EC.presence_of_element_located((By.ID, "docType"))))
        select.select_by_visible_text('Resume - .pdf, .doc or .docx')
    except TimeoutException as ex:
        print("Error doc type", str(ex))
    except Exception as e:
        print(str(e))


    submit = driver.find_element(By.ID, 'submitFileUploadFormBtn')

    file_elem = driver.find_element(By.ID, 'fileUpload_docUpload')
    file_elem.send_keys(os.path.join(resumes, file))
   
    wait_for_disable(submit)   
    wait_for_enable(submit)
    
    submit.click()
    
    time.sleep(0.1)
    bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))
    
    for btn in bottons:
        if btn.text == 'Upload Document':
            btn.click()
            break
    return

def wait_for_enable(element):
    count = 0
    while element.get_attribute('disabled') == 'true':
        if element.get_attribute('disabled') != 'true':
            break
        if count >= 100:
            break
        count += 1
        time.sleep(0.1)

def wait_for_disable(element):
    count = 0 
    while element.get_attribute('disabled') != 'true':
        if element.get_attribute('disabled') == 'true':
            break
        if count >= 100:
            break
        count += 1
        time.sleep(0.1)