import pytest
from .StepicPageObject.main_page import MainPage

class TestMainPage:  # Класс для тестов
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # Открываем страницу
        page.go_to_login_page()          # Выполняем метод страницы — переходим на страницу логина
