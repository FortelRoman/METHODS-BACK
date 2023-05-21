from selenium.webdriver.common.by import By
from selenium import webdriver
import time

path = 'http://127.0.0.1:3000/votes/simple'
options = {'Q1': 'id-3', 'Q2': 'id-3', 'Q3': 'id-3', 'Q4': 'id-3', 'Q5': 'id-3'}

driver = webdriver.Chrome()
driver.get(path)

for key, value in options.items():
    selector = f'''
            input[name="{key}"][value="{value}"]
        '''
    driver.find_element(By.CSS_SELECTOR, selector).click()

saveButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
saveButton.click()

time.sleep(30)
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