import time

from select import select
from selenium import webdriver
from selenium.webdriver.chromium import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


driver =webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[1]/button").click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(3)
