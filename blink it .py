from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://blinkit.com/?srsltid=AU7gw4XRgZPPlqsBk_BKu5592mZoLdYaBa1XF7bEojQizyjrtdExN74X")
driver.maximize_window()
time.sleep(2)
#view the location
location=driver.find_element(By.NAME,"select-locality")
location.click()
#select the location
location.send_keys("Guru Theatre")
time.sleep(3)
GuruTheatre=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[1]/header/div[2]/div[2]/div/div/div[2]/div/div/div[1]")
GuruTheatre.click()
time.sleep(2)
#select the fast food
food=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[3]/div/div[3]/div/div/div/div[6]/img")
food.click()
time.sleep(3)
#select the chocos
chocos=driver.find_element(By.XPATH,"//*[@id='758013']/div[2]/div/img")
chocos.click()
time.sleep(3)
#select the items
addcart=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div")
addcart.click()
time.sleep(3)
