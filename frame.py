import time

from selenium import webdriver
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(3)
element=driver.find_element(By.ID,"singleframe")
driver.switch_to.frame(element)
element=driver.find_element(By.XPATH,"/html/body/section/div/div/div/input")
element.send_keys("sethu")
time.sleep(3)
