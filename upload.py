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
    # try:
    #     file_elem = driver.find_element(By.ID, 'fileUpload_docUpload')
    #     file_elem.send_keys(os.path.join(cover_letters, file))
    # except Exception as e:
    #     print('File upload error\n' ,str(e))

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

    #print('Waiting for disabled:')
    wait_for_disable(submit)
    #print('Should be disabled:',submit.get_attribute('disabled'))
    #print(type(submit.get_attribute('disabled')))
    wait_for_enable(submit)
    #print('out of wait')
    submit.click()

def upload_resume(driver, file):
    wait = WebDriverWait(driver, 10)
    # try:
    #     file_elem = driver.find_element(By.ID, 'fileUpload_docUpload')
    #     file_elem.send_keys(os.path.join(cover_letters, file))
    # except Exception as e:
    #     print('File upload error\n' ,str(e))

    try:
        name = wait.until(EC.presence_of_element_located((By.ID,'docName')))
        name.send_keys('Cover_Letter')

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
    file_elem.send_keys(os.path.join(cover_letters, file))

    #print('Waiting for disabled:')
    wait_for_disable(submit)
    #print('Should be disabled:',submit.get_attribute('disabled'))
    #print(type(submit.get_attribute('disabled')))
    wait_for_enable(submit)
    #print('out of wait')
    submit.click()

def wait_for_enable(element):
    #print('waiting to enable:', element.get_attribute('disabled'))
    while element.get_attribute('disabled') == 'true':
        #print('waiting to enable:', element.get_attribute('disabled'))
        if element.get_attribute('disabled') != 'true':
            break
        time.sleep(0.1)

def wait_for_disable(element):
    #print('waiting to disable:', element.get_attribute('disabled'))
    while element.get_attribute('disabled') != 'true':
        #print('waiting to disable:', element.get_attribute('disabled'))
        if element.get_attribute('disabled') == 'true':
            break
        time.sleep(0.1)