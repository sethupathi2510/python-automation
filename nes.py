import time

from selenium import webdriver
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(3)
nested=driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a")
nested.click()
time.sleep(3)
nested=driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(nested)
nested=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(nested)
nested=driver.find_element(By.XPATH,"/html/body/section/div/div/div/input")
nested.send_keys("sethu")
time.sleep(3)