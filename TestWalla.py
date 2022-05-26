import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.walla.co.il/')
time.sleep(5)


link = driver.find_element_by_link_text("כסף")
link.click()
time.sleep(10)

rate = driver.find_element_by_class_name("rate")
print(rate.text)


# driver.quit()
# python MikaTest.py
# C:\Users\mika.m\OneDrive\Desktop\website_login>
