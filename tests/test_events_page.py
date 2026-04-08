import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class GreenCityTests(unittest.TestCase):

    def setUp(self):
        # налаштування
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def tearDown(self):
        self.driver.quit()

    def test_0_check_connection(self):
        """базова перевірка: чи завантажився сайт"""
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("\n[OK] сайт  завантажився")

    def test_tc1_registration(self):
        """TC-1: Реєстрація нового користувача (Sign Up)"""
        
        # створюємо унікальну пошту за допомогою цифр часу(щоб не було помилок під час тестування)
        unique_email = f"tester_max_{int(time.time())}@gmail.com"
        
        # 1 клік на Sign up у хедері
        sign_up_header = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(), 'Sign up')]")
        ))
        sign_up_header.click()

        # 2 заповнення полів
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_field.send_keys(unique_email)

        user_name_field = self.driver.find_element(By.ID, "firstName")
        user_name_field.send_keys("TesterMax") 

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Qwerty12345!") 

        confirm_password_field = self.driver.find_element(By.ID, "repeatPassword")
        confirm_password_field.send_keys("Qwerty12345!")

        # 3 перевірка активності кнопки
        final_sign_up_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        self.assertTrue(final_sign_up_btn.is_enabled(), "помилка (кнопка не спрацювала через помилку в заповненні полів)")
        
        print(f"\n[OK] Тест TC-1 пройдено з поштою: {unique_email}")

    def test_tc2_filter_upcoming(self):
        """TC-2: Фільтрація подій за статусом 'Upcoming'"""
        
        # 1 відкриваємо випадаючий список Event time
        filter_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//mat-label[contains(text(), 'Event time')]")
        ))
        filter_button.click()

        # 2 обираємо варіант Upcoming
        upcoming_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(), 'Upcoming')]")
        ))
        upcoming_option.click()

        # 3 Assert
        active_chip = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Upcoming')]")
        ))
        
        self.assertTrue(active_chip.is_displayed(), "Фільтр 'Upcoming' не був застосований")
        
        print("\n[OK] Тест TC-2 пройдено: фільтрація працює")

    def test_tc3_sign_in(self):
        """TC-3: Авторизація користувача (перевірка за рейтингом)"""
        
        # 1 натискаємо Sign in у хедері
        sign_in_link = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "header_sign-in-link")
        ))
        sign_in_link.click()

        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_input.send_keys("Maksym.Huliaiev@lnu.edu.ua")
        
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("PesMops@2014")

        # 2 тиснемо кнопку входу
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        # Очікуємо появу елемента з класом rate
        user_rate = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "rate")
        ))
        
        # Перевіряємо, чи текст містить Rate
        self.assertIn("Rate:", user_rate.text, "Вхід не відбувся: рейтинг користувача не знайдено")
        
        print(f"\n[OK] Тест TC-3 пройдено")

if __name__ == "__main__":
    unittest.main()