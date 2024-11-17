from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


def login(user, secret, search):

    driver = webdriver.Firefox()
    driver.get("https://myexperience.sfu.ca/notLoggedIn.htm")
    
    elem = driver.find_element(By.LINK_TEXT, "Student")
    
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
        nav = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Exp. Learning (Co-op)")))
        time.sleep(1)
        nav.click()

    except TimeoutException as ex:
        print("Error exp", str(ex))
    except Exception as e:
        print(str(e))

    open_documents(driver)   

    try:
        nav = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Job Postings")))
        
        nav.click()
        
    except TimeoutException as ex:
        print("Error Job", str(ex))
    except Exception as e:
        print(str(e))

    try:
        select = Select(wait.until(EC.presence_of_element_located((By.ID, "savedSearchId"))))
        select.select_by_visible_text(search)
    except TimeoutException as ex:
        print("Error: No such custom saved search", search)
    except Exception as e:
        print(str(e))
    
    try:
        if wait.until(EC.title_contains('Job Postings')):
            return driver
        else:
            print(driver.title)
    except Exception as e:
        print(str(e))
    
    return None


def open_documents(driver):
    wait = WebDriverWait(driver, 10)
    try:
        nav = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Documents")))
        action = ActionChains(driver)

        action.key_down(Keys.LEFT_CONTROL)
        action.click(nav)
        action.key_up(Keys.LEFT_CONTROL)
        action.perform()
        
        
    except TimeoutException as ex:
        print("Error Documents", str(ex))
    except Exception as e:
        print(str(e))
    
    driver.switch_to.window(driver.window_handles[-1])
    bottons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-primary')))
    for btn in bottons:
        if btn.text == 'Upload Document':
            btn.click()
            break
    driver.switch_to.window(driver.window_handles[0])
    return