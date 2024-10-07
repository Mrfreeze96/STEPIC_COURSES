import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nRunning tests in {language} language..")
    yield language
