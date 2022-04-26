from time import time
from webbrowser import Chrome
from jmespath import search
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def iniciar_chrome():
    ruta = ChromeDriverManager(path='./chromedriver', log_level=0).install()
    
    options = Options()
    options.add_argument("--disable-web-security")
    options.add_argument("--no-sandbox")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    # jaque mate
    options.add_argument("--disable-blink-features=AutomationControlled")

    opc = ['enable-automation']
    options.add_experimental_option("excludeSwitches", opc)

    prefs = {"intl.accept_languages": ["es-ES", "es"]}
    options.add_experimental_option("prefs", prefs)

    s = Service(ruta)
    # os.environ['PATH'] += "C:/Users/3940/Documents/pedidosSha/resources/chromedriver.exe"
    driver = webdriver.Chrome(service=s, options=options)
    return driver

if __name__ == '__main__':
    driver = iniciar_chrome()
    url = "https://www.pedidosya.com.uy/"
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(2)
    ubi = driver.find_element(By.ID, "search_address_input")
    ubi.send_keys("bv artigas 1127")
    ubi.send_keys(Keys.RETURN)
   # conf = WebDriverWait(driver, 15).until(
       # EC.presence_of_element_located(By.ID, "confirm_location_btn"))
    time.sleep(5)
    conf = driver.find_element(By.ID, "confirm_location_btn")
    #conf.click()
    print(driver.get_cookies())
    time.sleep(2)
    #driver.quit()