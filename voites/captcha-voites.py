from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

settings = {
    'Q1': 'id-3',
    'Q2': 'id-3',
    'Q3': 'id-3',
    'Q4': 'id-3',
    'Q5': 'id-3',
}


DRIVER_PATH = './msedgedriver.exe'
path = 'http://127.0.0.1:3000/'

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Edge(options=options, executable_path=DRIVER_PATH)
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

time.sleep(30)

driver.quit()