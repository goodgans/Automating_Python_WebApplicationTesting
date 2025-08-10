import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_post_ui(driver, config):
    wait = WebDriverWait(driver, 20)

    driver.get(config["address"] + "/login")

    username_input = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//label[.//span[contains(text(), 'Username')]]//input"
    )))
    username_input.send_keys(config["username"])

    password_input = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//label[.//span[contains(text(), 'Password')]]//input"
    )))
    password_input.send_keys(config["password"])

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.url_to_be(config["address"] + "/"))

    create_post_button = wait.until(EC.element_to_be_clickable((By.ID, "create-btn")))
    create_post_button.click()

    wait.until(EC.url_contains("/posts/create"))

    unique_title = f"Тестовый пост {random.randint(1000, 9999)}"
    unique_description = f"Описание {random.randint(1000, 9999)}"
    content_text = "Автотест контент"

    title_input = wait.until(EC.presence_of_element_located((
        By.XPATH, "//label[.//span[text()='Title']]//input"
    )))
    title_input.send_keys(unique_title)

    description_input = wait.until(EC.presence_of_element_located((
        By.XPATH, "//label[.//span[text()='Description']]//textarea"
    )))
    description_input.send_keys(unique_description)

    content_input = wait.until(EC.presence_of_element_located((
        By.XPATH, "//label[.//span[text()='Content']]//textarea"
    )))
    content_input.send_keys(content_text)

    save_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[text()='Save']]"
    )))
    save_button.click()

    time.sleep(3)

    page_source = driver.page_source
    assert unique_title in page_source, f"Заголовок '{unique_title}' не найден на странице"

    print(f"Пост '{unique_title}' успешно создан и отображается на странице.")