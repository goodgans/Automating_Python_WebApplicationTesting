import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def config():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture(scope="session")
def login(config):
    response = requests.post(
        f"{config['address']}/gateway/login",
        data={"username": config["username"], "password": config["password"]}
    )
    response.raise_for_status()
    return response.json().get("token")


@pytest.fixture
def driver(config):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()