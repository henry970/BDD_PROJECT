from behave import given, when, then
from selenium import webdriver
from pages.base_page import BasePage

from selenium.webdriver.chrome.options import Options


@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration

    context.driver = webdriver.Chrome(options=chrome_options)
    context.page = BasePage(context.driver)
    context.page.navigate_to_login_page()


# @given('I am on the login page')
# def step_given_i_am_on_the_login_page(context):
#     context.driver = webdriver.Chrome()
#     context.page = BasePage(context.driver)
#     context.page.navigate_to_login_page()


@when('I enter valid credentials')
def step_when_i_enter_valid_credentials(context):
    context.page.enter_credentials('test@gmail.com', 'password')


@when('I click the login button')
def step_when_i_click_the_login_button(context):
    context.page.click_login_button()
