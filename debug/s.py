#!/usr/bin/python3
import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"
option = webdriver.ChromeOptions()
option.binary_location = binary_location
# Here Chrome  will be used
driver = webdriver.Chrome(executable_path=driver_location, chrome_options=option)

# URL of website
url = "https://www.olx.uz/d/obyavlenie/ijaraga-xonadon-beriladi-ID2USqZ.html"

# Opening the website
driver.get(url)

# getting the button by class name
button = driver.find_element(By.CSS_SELECTOR, 'button.css-unrcts-BaseStyles')

# # clicking on the button
button.click()