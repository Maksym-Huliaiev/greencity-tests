from src.pages.base_page import BasePage
from src.components.header import Header
from src.components.filter_panel import FilterPanel
from selenium.webdriver.common.by import By

class EventsPage(BasePage):
    USER_RATE = (By.CLASS_NAME, "rate")

    def __init__(self, driver):
        super().__init__(driver)
        # Ініціалізація компонентів для доступу через крапку
        self.header = Header(driver)
        self.filter_panel = FilterPanel(driver)