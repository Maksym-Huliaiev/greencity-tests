from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure

class Header(BaseComponent):
    SIGN_UP_HEADER = (By.XPATH, "//span[contains(text(), 'Sign up')]")
    SIGN_IN_LINK = (By.CLASS_NAME, "header_sign-in-link")
    
    EMAIL_INPUT = (By.ID, "email")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASS_INPUT = (By.ID, "repeatPassword")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Відкрити форму реєстрації")
    def start_registration(self):
        self.click(self.SIGN_UP_HEADER)

    @allure.step("Заповнити форму реєстрації")
    def fill_registration(self, email, name, password):
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.FIRST_NAME_INPUT).send_keys(name)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.CONFIRM_PASS_INPUT).send_keys(password)

    @allure.step("Авторизуватися в системі")
    def sign_in(self, email, password):
        self.click(self.SIGN_IN_LINK)
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.click(self.SUBMIT_BTN)