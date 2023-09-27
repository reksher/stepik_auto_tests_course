from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x2 = x1
    x3 = calc(x2)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x3)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()