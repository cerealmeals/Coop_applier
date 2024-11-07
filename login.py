from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


def login(user, secret):

    driver = webdriver.Firefox()
    driver.get("https://myexperience.sfu.ca/notLoggedIn.htm")
    #print(driver.title)
    elem = driver.find_element(By.LINK_TEXT, "Student")
    #print(elem)
    elem.click()

    wait = WebDriverWait(driver, 20)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    username.send_keys(user)
    password.send_keys(secret)
    password.submit()

    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.title_contains('myExp'))
    wait = WebDriverWait(driver, 1)
    try:
        code = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Exp. Learning (Co-op)")))
        time.sleep(0.1)
        code.click()

    except TimeoutException as ex:
        print("Error exp", str(ex))
    except Exception as e:
        print(str(e))

    try:
        code = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Job Postings")))
        
        code.click()
        
    except TimeoutException as ex:
        print("Error Job", str(ex))
    except Exception as e:
        print(str(e))

    try:
        select = Select(wait.until(EC.presence_of_element_located((By.ID, "savedSearchId"))))
        select.select_by_visible_text('normal')
    except TimeoutException as ex:
        print("Error savedsearchs", str(ex))
    except Exception as e:
        print(str(e))
    
    try:
        if wait.until(EC.title_contains('Job Postings')):
            return driver
        else:
            print(driver.title)
    except Exception as e:
        print(str(e))
    
    print(driver.title)
    return None
