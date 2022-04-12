import os
from selenium import webdriver

os.environ['PATH'] += "C:/Users/3940/Documents/selenium/resources/chromedriver.exe"
driver = webdriver.Chrome(
    "C:/Users/3940/Documents/selenium/resources/chromedriver.exe")
driver.get("https://www.pedidosya.com.uy/")
# wait before asking elem id just in case browser is slow (or to seem like a human)
driver.implicitly_wait(3)
dire = driver.find_element_by_id("search_address_input")
dire.click()