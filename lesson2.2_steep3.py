from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x2 = x1

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x3 = calc(x2)

    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(x3)

    checkbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton1.click()

    browser.find_element(By.CSS_SELECTOR, ".btn").click()




finally:
    time.sleep(10)
    browser.quit()

