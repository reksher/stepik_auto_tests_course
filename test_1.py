from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
class TestLink(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("stanislav")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("sannikov")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("test@test.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test passed")

    def test_link2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("stanislav")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("sannikov")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("test@test.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test passed")
if __name__ == "__main__":
    unittest.main()
