import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def config():
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def auth_token(config):
    url = config['url_login']
    data = {
        "username": config['default']['username'],
        "password": config['default']['password']
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Не удалось получить токен, статус: {response.status_code}, ответ: {response.text}"
    token = response.json().get("token")
    assert token is not None, "Токен не найден в ответе"
    return token

@pytest.fixture
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()