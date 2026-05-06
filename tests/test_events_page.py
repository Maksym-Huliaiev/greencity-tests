import allure
import pytest
import time
from src.pages.events_page import EventsPage

@allure.feature("GreenCity Events UI")
@allure.story("Registration, Filters and Authorization")
class TestEvents:

    def test_tc1_registration(self, driver):
        driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        page = EventsPage(driver)
        unique_email = f"tester_max_{int(time.time())}@gmail.com"

        with allure.step("Реєстрація нового користувача"):
            page.header.start_registration()
            page.header.fill_registration(unique_email, "TesterMax", "Qwerty12345!")
        
        with allure.step("Перевірка активності кнопки Sign Up"):
            submit_btn = page.find_element(page.header.SUBMIT_BTN)
            assert submit_btn.is_enabled()

    def test_tc2_filter_upcoming(self, driver):
        driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        page = EventsPage(driver)

        with allure.step("Застосування фільтра Upcoming"):
            page.filter_panel.filter_by_upcoming()
            
        with allure.step("Перевірка відображення фільтра"):
            active_chip = page.find_element(page.filter_panel.ACTIVE_FILTER)
            assert active_chip.is_displayed()

    def test_tc3_sign_in(self, driver):
        driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        page = EventsPage(driver)

        with allure.step("Вхід в існуючий акаунт"):
            page.header.sign_in("Maksym.Huliaiev@lnu.edu.ua", "PesMops@2014")
            
        with allure.step("Перевірка успішної авторизації"):
            user_rate = page.find_element(page.USER_RATE)
            assert "Rate:" in user_rate.text