from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
import time

DRIVER_PATH = './chromedriver.exe'
path = 'http://127.0.0.1:3001/votes/browser'

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])


service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(options=options, dri)
# driver = uc.Chrome(version_main = 112)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#     '''
# })

driver.get(path)


# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox")))
# time.sleep(3)

# for key, value in settings.items():
#     print(key, "=>", value)
#
#     selector = f'''
#             input[name="{key}"][value="{value}"]
#         '''
#     driver.find_element(By.CSS_SELECTOR, selector).click()

time.sleep(1)
#
driver.find_element(By.CSS_SELECTOR, 'button[id="1"]').click()

# driver.find_element(By.CSS_SELECTOR, 'button[id="2"]').click()
#
# time.sleep(1)
# el = driver.find_element(By.CSS_SELECTOR, 'div[id="root"]')
# print(el.text)


time.sleep(2330)
driver.quit()



# iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
# driver.switch_to.frame(iframe)
#
# check = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox')
# check.click()
#
# time.sleep(3)
#
# text = driver.find_element(By.CLASS_NAME, 'text').text;
# print(text)