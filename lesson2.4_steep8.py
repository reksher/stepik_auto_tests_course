from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    #данная часть кода не возвращает ничего, просто условие, что мы ищем в течение 12 секунд значение 100
    button.click()

    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x2 = x1


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x3 = calc(x2)

    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x3)

    input2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    input2.click()





finally:

    time.sleep(10)
    browser.quit()
