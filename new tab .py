from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
driver.maximize_window()
time.sleep(3)
main_window=driver.current_window_handle
driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[1]").click()
time.sleep(3)
windows=driver.window_handles
for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        break
print("new tab name:", driver.name)
time.sleep(3)
new=driver.find_element(By.XPATH,"/html/body/div/header/div[3]/a").click()
time.sleep(3)