import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import driver_finder, actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://vinothqaacademy.com/mouse-event/")
action=ActionChains(driver)
driver.maximize_window()
time.sleep(3)
element=driver.find_element(By.ID,"doubleBtn")
action.double_click(element).perform()
time.sleep(3)
element=driver.find_element(By.ID,"rightBtn")
action.context_click(element).perform()
time.sleep(3)
element=driver.find_element(By.ID,"tooltipTarget")
action.click_and_hold(element).perform()
source=driver.find_element(By.ID,"dragItem")
target=driver.find_element(By.ID,"dropZone")
action.drag_and_drop(source,target).perform()
time.sleep(3)
element=driver.find_element(By.ID,"tooltipTarget")
action.click_and_hold(element).perform()
time.sleep(3)
driver.close()
driver=webdriver.Chrome()
driver.switch_to.new_window('tab')
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(3)

