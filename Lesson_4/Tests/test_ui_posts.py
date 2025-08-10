import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_create_post_ui(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://test-stand.gb.ru/login")

    username_input = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//label[span[contains(text(), 'Username')]]//input[contains(@class, 'mdc-text-field__input')]"
    )))
    username_input.send_keys("samec24")

    password_input = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//label[span[contains(text(), 'Password')]]//input[contains(@class, 'mdc-text-field__input')]"
    )))
    password_input.send_keys("ТвойПароль")

    login_button = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        "#login > div.submit.svelte-uwkxn9 > button"
    )))
    login_button.click()

   
