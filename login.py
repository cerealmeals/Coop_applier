from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

user = 'shn9'

driver = webdriver.Firefox()
driver.get("https://myexperience.sfu.ca/notLoggedIn.htm")
print(driver.title)
elem = driver.find_element(By.LINK_TEXT, "Student")
print(elem)
elem.click()
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
time.sleep(20)

driver.close()