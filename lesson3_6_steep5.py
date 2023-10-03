import time
import pytest
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


linkss = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]
@pytest.mark.parametrize('links', linkss)
def test_autorization_in_stepik(browser, links):
        browser.get(links)
        WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.ID, 'ember33'))).click()
        browser.find_element(By.CSS_SELECTOR, "[placeholder='E-mail']").send_keys('почта')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']").send_keys('пароль')
        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
        time.sleep(2)
        WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea'))).send_keys(str(math.log(int(time.time()))))
        WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()
        output_message = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
        assert "Correct!" == output_message, f"incorrect, {output_message}"









