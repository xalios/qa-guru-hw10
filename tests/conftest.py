import pytest
from os import path
from selene import browser

RES_DIR = path.abspath(path.join(path.dirname(__file__), 'resources'))

@pytest.fixture(scope='function', autouse=True)
def chrome_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
