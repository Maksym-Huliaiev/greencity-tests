from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure

class FilterPanel(BaseComponent):
    FILTER_BTN = (By.XPATH, "//mat-label[contains(text(), 'Event time')]")
    UPCOMING_OPT = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    ACTIVE_FILTER = (By.XPATH, "//*[contains(text(), 'Upcoming')]")

    @allure.step("Обрати фільтр 'Upcoming'")
    def filter_by_upcoming(self):
        self.click(self.FILTER_BTN)
        self.click(self.UPCOMING_OPT)