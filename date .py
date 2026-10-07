from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

'''driver.find_element(By.ID,"datepicker").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']").click()
time.sleep(2)

driver.find_element(By.ID,"txtDate").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/select[1]/option[5]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/select[2]/option[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
time.sleep(2)'''

date=driver.find_element(By.XPATH,"//*[@id='start-date']")
date.send_keys("29/02/2009")
time.sleep(2)
another=driver.find_element(By.ID,"end-date")
another.send_keys("29/03/2030")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"submit-btn").click()
time.sleep(2)
