import time

from select import select
from selenium import webdriver
from selenium.webdriver.chromium import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver =webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(3)
name=driver.find_element(By.TAG_NAME, "input")
#name=driver.find_element(BY.NAME,"name")
name.send_keys("sethupathi")
time.sleep(3)
name=driver.find_element(By.ID, "email")
name.send_keys("sethusk@gamil.com")
time.sleep(3)
search=driver.find_element(By.NAME, "gender")
search.send_keys("male")
search.click()
time.sleep(3)
mobile=driver.find_element(By.ID, "mobile")
mobile.send_keys("123456789")
time.sleep(3)
date=driver.find_element(By.ID, "dob")
date.send_keys("03/04/2003")
time.sleep(3)
sub=driver.find_element(By.XPATH, "//*[@id='subjects']")
sub.send_keys("python")
upload=driver.find_element(By.XPATH, "//input[@type='file']")
upload.send_keys("C:/Users/STAR/Desktop/sethu.txt")
time.sleep(3)
state=driver.find_element(By.ID,"state")
dd=Select(state)
dd.select_by_visible_text("Haryana")
time.sleep(3)
city=driver.find_element(By.ID,"city")
dd=Select(city)
dd.select_by_index(1)
time.sleep(3)
















