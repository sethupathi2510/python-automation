import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://practice-automation.com/popups/")
driver.maximize_window()
time.sleep(3)
prompt=driver.find_element(By.ID,"prompt")
prompt.click()
time.sleep(3)
alert=driver.switch_to.alert
alert.send_keys("Sethupathy")
time.sleep(3)
alert.accept()
time.sleep(3)
