import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    chrome_options = webdriver.ChromeOptions()
    # Указываем опцию headless=False для визуального отображения браузера
    chrome_options.headless = False
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()