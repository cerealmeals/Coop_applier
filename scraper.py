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



def createFile(driver):
    wait = WebDriverWait(driver, 10)
    try:
        title_elem = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'dashboard-header__profile-information-name')))
        title = title_elem[0].text
        #print(title, title)
    except Exception as e:
        print('title error\n' ,str(e))
    
    
    print('Creating file for job', title)
    current = os.path.dirname(os.path.abspath(__file__))
    current = os.path.join(current, 'Jobs')
    if not os.path.exists(current):
        os.makedirs(current)
    
    print('at file path', current)
    filepath = os.path.join(current, title)
    try:
        f = open(filepath, "w")
        
        try:
            elements = driver.find_elements(By.TAG_NAME, 'tr')
            #print('how many elements walking through:', len(elements))
            for elem in elements:
                f.write(elem.text + '#\n')
            
        except Exception as e:
            print('tr error\n',str(e))
        
        f.close()
    except Exception as e:
        print('file Error',str(e))

    return title


    