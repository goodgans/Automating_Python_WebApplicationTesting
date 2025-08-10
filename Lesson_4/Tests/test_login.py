from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

def test_login_and_redirect_to_homepage(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://test-stand.gb.ru/login")


    username_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='login']//label[.//span[contains(text(),'Username')]]//input")
    ))
    username_input.send_keys("samec24")

    password_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='login']//label[.//span[contains(text(),'Password')]]//input")
    ))
    password_input.send_keys("b6a9c7f893")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login']//button")))
    login_button.click()

    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1.text == "Blog", "Не удалось перейти на домашнюю страницу"
    logger.info("Успешный вход и переход на домашнюю страницу")