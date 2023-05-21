from selenium.webdriver.common.by import By
from selenium import webdriver

path = 'http://127.0.0.1:3000/parse/simple'
driver = webdriver.Chrome()
driver.get(path)

speciality = driver.find_element(By.CSS_SELECTOR, "h1.page__title")
print('Специальность: ', speciality.text)

content = driver.find_element(By.CSS_SELECTOR, "div.page__content")
print('\n' + content.text)

driver.quit()
