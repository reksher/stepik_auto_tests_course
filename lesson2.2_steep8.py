from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    name.send_keys('Stanislav')

    lastname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    lastname.send_keys('Sannikov')

    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    email.send_keys('test@test.ru')

    directory = os.path.abspath(os.path.dirname('C:/Users/Слава/Desktop/'))
    name_file = os.path.join(directory, 'test.txt')
    send_file = browser.find_element(By.CSS_SELECTOR, "#file")
    send_file.send_keys(name_file)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

