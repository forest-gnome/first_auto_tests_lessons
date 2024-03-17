from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

PAGES_BUTTON = (By.XPATH, '//*[@aria-label="Поиск картинок (откроется новая вкладка)"]')

driver = webdriver.Chrome()

def find_element(driver, locator, time=5):
    return WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(locator))

def test_error_auth():
    driver.get("https://google.com")
    find_element(driver, PAGES_BUTTON).click()