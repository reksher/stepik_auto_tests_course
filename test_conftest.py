import time
import pytest
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_autorization_in_stepik(browser):
    browser.get('https://stepik.org/lesson/236897/step/1')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ember33'))).click()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='E-mail']").send_keys('stanislav-sannicov@mail.ru')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']").send_keys('130877best')
    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
    time.sleep(1)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]'))).send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    output_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    output_message_corr = str(output_message)
    print(output_message_corr)
