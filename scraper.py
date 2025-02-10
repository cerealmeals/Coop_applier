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



def scraper(driver):
    wait = WebDriverWait(driver, 10)
    try:
        title_elem = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'dashboard-header__profile-information-name')))
        title = title_elem[0].text
        title = check_for_valid_file_name(title)
    except Exception as e:
        print('title error\n' ,str(e))
    
    try:
        WebDriverWait(driver, 0.01).until(EC.presence_of_element_located((By.CLASS_NAME,'applyButton')))
    except Exception as e:
        print("No apply button for job", title)
        return "NONE"
    print('Creating file for job', title)
    current = os.path.dirname(os.path.abspath(__file__))
    current = os.path.join(current, 'Jobs')
    if not os.path.exists(current):
        os.makedirs(current)
    
    
    filepath = os.path.join(current, title)
    print('at file path', filepath)
    try:
        f = open(filepath, "w")
        
        try:
            elements = driver.find_elements(By.TAG_NAME, 'tr')
            
            for elem in elements:
                f.write(elem.text + '#\n')
            
        except Exception as e:
            print('tr error\n',str(e))
        
        f.close()
    except Exception as e:
        print('file Error',str(e))

    return title


def check_for_valid_file_name(string):
    list_of_bad = ['>', '<', ':', '\"', '/', '\\', '|', '?', '*']
    index_of_bad = []
    check = list(string)
    for i, ch in enumerate(check):
        if ch in list_of_bad:
            index_of_bad.append(i)
    for i in range(len(index_of_bad)-1, -1, -1):
        check.pop(index_of_bad[i])
    string = ''.join(check)
    return string