from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time


DRIVER_PATH = './msedgedriver.exe'
path = 'http://127.0.0.1:3000/'

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Edge(options=options, executable_path=DRIVER_PATH)
driver.get(path)


# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox")))
time.sleep(3)
iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
driver.switch_to.frame(iframe)

check = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox')
check.click()

time.sleep(3)

text = driver.find_element(By.CLASS_NAME, 'text').text;
print(text)

#
# vacancies = driver.find_elements_by_class_name('vacancies-list-item__link_block')
#
# nextVacancy = "Вакансия " + vacancies[0].text;
#
# for index in range(len(vacancies)):
#
#     vacancies[index].click();
#
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "title"))
#     )
#
#     if (index > 0): {
#         WebDriverWait(driver, 20).until(
#             EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), nextVacancy)
#         )
#     }
#
#     vacancy = {}
#     vacancyName = driver.find_element_by_class_name('title').text
#     vacancy['Название'] =  vacancyName[vacancyName.find(" ") + 1:]
#     vacancy['Ссылка'] = vacancies[index].get_attribute("href")
#     vacancy['Cкилы'] = driver.find_element_by_class_name('vacancy__tags').text.split('\n')
#     vacancy['Описание'] = driver.find_element_by_class_name('vacancy__text').get_attribute('innerHTML')
#     vacancy['Компания'] = driver.find_element_by_class_name('vacancy__header__company-name').text
#
#     info = driver.find_element_by_class_name('vacancy__info').text.split('\n')
#
#     for i in range(len(info)):
#         keyAndValue = info[i].split(': ')
#         key = keyAndValue[0]
#         value = keyAndValue[1]
#         vacancy[key] = value
#
#     setSalary(vacancy)
#
#     if 'Режим работы' not in vacancy:
#         vacancy['Режим работы'] = 'Не указан'
#
#     if 'Размер компании' not in vacancy:
#         vacancy['Размер компании'] = -1
#
#     if 'Возможна удалённая работа' not in vacancy:
#         vacancy['Возможна удалённая работа'] = 'Не указано'
#
#     if vacancy["Cкилы"][0] == '':
#         vacancy["Cкилы"] = ['Не требуются']
#
#     for i in vacancy:
#         if isinstance(vacancy[i], str):
#             vacancy[i] = vacancy[i].replace('"', "'")
#
#     query = f'''
#         CREATE (vacancy{index} :vacancy{{vacancy: "{vacancy['Название']}", link: "{vacancy['Ссылка']}", salary_from: {vacancy['Зарплата от']}, salary_to: {vacancy['Зарплата до']}, description: "{vacancy['Описание']}"}})
#         MERGE (specialization{index} :specialization{{specialization:"{vacancy['Специализация']}"}})
#         MERGE (city{index} :city{{city:"{vacancy['Город']}"}})
#         MERGE (level{index} :level{{level:"{vacancy['Уровень']}"}})
#         MERGE (english_level{index} :english_level{{english_level:"{vacancy['Уровень английского']}"}})
#         MERGE (experience{index} :experience{{experience:"{vacancy['Опыт']}"}})
#         MERGE (work_time{index} :work_time{{work_time:"{vacancy['Режим работы']}"}})
#         MERGE (distance_work{index} :distance_work{{distance_work:"{vacancy['Возможна удалённая работа']}"}})
#         MERGE (company{index} :company{{company:"{vacancy['Компания']}", company_size: {vacancy['Размер компании']}}})
#
#         CREATE (vacancy{index})-[: has_specialization]->(specialization{index})
#         CREATE (vacancy{index})-[: located_in]->(city{index})
#         CREATE (vacancy{index})-[: has_level]->(level{index})
#         CREATE (vacancy{index})-[: has_english_level]->(english_level{index})
#         CREATE (vacancy{index})-[: has_experience]->(experience{index})
#         CREATE (vacancy{index})-[: has_work_time]->(work_time{index})
#         CREATE (vacancy{index})-[: has_distance_work]->(distance_work{index})
#         CREATE (vacancy{index})-[: in_company]->(company{index})
#     '''
#
#     for i in range(len(vacancy['Cкилы'])):
#         query += f'''
#             MERGE (skill{index}_{i} :skill{{skill:"{vacancy["Cкилы"][i]}"}})
#             MERGE (vacancy{index})-[: need_skill]->(skill{index}_{i})
#         '''
#
#     DB.add_vacancy(query)
#
#     if (index != len(vacancies)-1):
#         nextVacancy = "Вакансия " + vacancies[index+1].text
#
#     print(str(index+1) + '/' + str(len(vacancies)) + '    ' + str(round((index+1)/len(vacancies), 3)*100) + ' %')
#
# DB.close()
driver.quit()