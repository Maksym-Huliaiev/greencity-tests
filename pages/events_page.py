from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EventsPage(BasePage):
    SIGN_UP_HEADER = (By.XPATH, "//span[contains(text(), 'Sign up')]")
    EMAIL_INPUT = (By.ID, "email")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASS_INPUT = (By.ID, "repeatPassword")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    
    FILTER_BTN = (By.XPATH, "//mat-label[contains(text(), 'Event time')]")
    UPCOMING_OPT = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    ACTIVE_FILTER = (By.XPATH, "//*[contains(text(), 'Upcoming')]")
    
    SIGN_IN_LINK = (By.CLASS_NAME, "header_sign-in-link")
    USER_RATE = (By.CLASS_NAME, "rate")

    def start_registration(self):
        self.click(self.SIGN_UP_HEADER)

    def fill_registration(self, email, name, password):
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.FIRST_NAME_INPUT).send_keys(name)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.CONFIRM_PASS_INPUT).send_keys(password)

    def filter_by_upcoming(self):
        self.click(self.FILTER_BTN)
        self.click(self.UPCOMING_OPT)

    def sign_in(self, email, password):
        self.click(self.SIGN_IN_LINK)
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.click(self.SUBMIT_BTN)