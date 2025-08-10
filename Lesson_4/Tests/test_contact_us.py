import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger("test_logger")
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_contact_us_alert(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://test-stand.gb.ru/login")

    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//input[contains(@class, 'mdc-text-field__input') and ancestor::label[span[contains(text(), 'Username')]]]"
        ))
    ).send_keys("samec24")

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    ).send_keys("b6a9c7f893")


    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    logger.info("Успешно вошли")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    driver.get("https://test-stand.gb.ru/contact")
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    name_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[span[text()='Your name']]//input"))
    )
    name_input.send_keys("Test User")


