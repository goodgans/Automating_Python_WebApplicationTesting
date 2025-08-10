import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_contact_us_alert(driver):
    wait = WebDriverWait(driver, 10)

    # Открытие страницы авторизации
    driver.get("https://test-stand.gb.ru/login")

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))).send_keys("samec24")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))).send_keys("b6a9c7f893")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mdc-button, div.mdc-button__ripple'))).click()

    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    # Переход на страницу Contact Us
    driver.get("https://test-stand.gb.ru/contact")
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    # Заполнение формы по порядку элементов
    wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="mdc-text-field__input"])[1]'))).send_keys("Test User")
    wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="mdc-text-field__input"])[2]'))).send_keys("test@example.com")
    wait.until(EC.visibility_of_element_located((By.XPATH, '(//textarea[@class="mdc-text-field__input"])[1]'))).send_keys("Сообщение для проверки формы.")

    # Нажатие на кнопку отправки
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    # Проверка alert
    alert = wait.until(EC.alert_is_present())
    print("Alert text:", alert.text)
    alert.accept()