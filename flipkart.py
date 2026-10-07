from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/mobile-phones-store?pageUID=1790833954089")
driver.maximize_window()
time.sleep(3)
mani_kart=driver.current_window_handle
print(mani_kart)
search=driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/header/div[1]/div[1]/form/div/div/input")
time.sleep(3)
search.send_keys("vivo",Keys.ENTER)
time.sleep(3)
for kart in mani_kart:
    if kart != mani_kart:
        driver.switch_to.window(mani_kart)
        break
print("new tab name:", driver.name)
time.sleep(3)
new=driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[3]/div[1]/div[1]")
new.click()
time.sleep(3)
