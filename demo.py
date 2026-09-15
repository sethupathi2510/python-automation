import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
driver.maximize_window()
time.sleep(3)
search=driver.find_element(By.NAME, "fullname")
search.send_keys("sethupathy")
time.sleep(3)

search=driver.find_element(By.ID, "email")
search.send_keys("sethusk17@gamil.com")
time.sleep(3)

search=driver.find_element(By.XPATH, "//*[@id='address']")
search.send_keys("thanichiyam north street madurai")
time.sleep(3)


