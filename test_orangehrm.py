from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)


def test_successful_login():
    driver = setup_driver()
    try:
        login(driver, "Admin", "admin123")
        time.sleep(2)

        dashboard_header = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        assert dashboard_header.is_displayed()
        print("Тест успішного входу пройдено")

        time.sleep(20)
    finally:
        driver.quit()


def test_invalid_login():
    driver = setup_driver()
    try:
        login(driver, "Admin", "wrongpassword")
        time.sleep(2)

        error_message = driver.find_element(By.XPATH, "//p[text()='Invalid credentials']")
        assert error_message.is_displayed()
        print("Тест неправильного входу пройдено")

        time.sleep(20)
    finally:
        driver.quit()


def test_navigation_to_my_info():
    driver = setup_driver()
    try:
        login(driver, "Admin", "admin123")
        time.sleep(2)

        my_info_link = driver.find_element(By.XPATH, "//span[text()='My Info']")
        my_info_link.click()
        time.sleep(2)

        url = driver.current_url
        assert "viewPersonalDetails" in url or "pim" in url.lower()
        print("Тест переходу на сторінку My Info пройдено")

        time.sleep(20)
    finally:
        driver.quit()