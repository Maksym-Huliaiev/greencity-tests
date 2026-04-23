import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.events_page import EventsPage # Імпортуємо наш Page Object

class GreenCityTests(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.page = EventsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_tc1_registration(self):
        unique_email = f"tester_max_{int(time.time())}@gmail.com"
        self.page.start_registration()
        self.page.fill_registration(unique_email, "TesterMax", "Qwerty12345!")
        
        submit_btn = self.page.find_element(self.page.SUBMIT_BTN)
        self.assertTrue(submit_btn.is_enabled())

    def test_tc2_filter_upcoming(self):
        self.page.filter_by_upcoming()
        active_chip = self.page.find_element(self.page.ACTIVE_FILTER)
        self.assertTrue(active_chip.is_displayed())

    def test_tc3_sign_in(self):
        self.page.sign_in("Maksym.Huliaiev@lnu.edu.ua", "PesMops@2014")
        user_rate = self.page.find_element(self.page.USER_RATE)
        self.assertIn("Rate:", user_rate.text)

if __name__ == "__main__":
    unittest.main()