from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
web.get("https://x.com/")
time.sleep(2)
sign_in = web.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
sign_in.click()
