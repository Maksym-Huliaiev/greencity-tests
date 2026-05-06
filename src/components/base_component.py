from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, locator):
        """Чекає, поки елемент з'явиться на сторінці[cite: 5]"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Чекає, поки на елемент можна буде клікнути[cite: 5]"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()