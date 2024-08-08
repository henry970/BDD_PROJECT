import time

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get('https://automationplayground.com/crm/login.html')

    def enter_credentials(self, email, password):
        self.driver.find_element(By.ID, 'email-id').send_keys(email)
        time.sleep(5)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(5)

    def click_login_button(self):
        self.driver.find_element(By.ID, 'submit-id').click()
        time.sleep(5)
