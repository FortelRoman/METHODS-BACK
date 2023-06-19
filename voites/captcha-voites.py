from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

settings = {
    'Q1': 'id-3',
    'Q2': 'id-3',
    'Q3': 'id-3',
    'Q4': 'id-3',
    'Q5': 'id-3',
}


DRIVER_PATH = './chromedriver-simple.exe'
path = 'http://127.0.0.1:3000/votes/captcha'

options = Options()
service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(options=options, service=service)
driver.get(path)

for key, value in settings.items():
    print(key, "=>", value)

    selector = f'''
            input[name="{key}"][value="{value}"]
        '''
    driver.find_element(By.CSS_SELECTOR, selector).click()

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(2)

iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
driver.switch_to.frame(iframe)

time.sleep(2)

check = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox')
check.click()

time.sleep(30000)

driver.quit()
