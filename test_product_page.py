import pytest
from .StepicPageObject.product_page import ProductPage

class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # Открываем страницу
        page.add_product_to_basket()   # Выполняем метод add_product_to_basket из файла product_page.py — добавляем товар в корзину
        page.solve_quiz_and_get_code()   # Решаем математическое выражение в алерте
        page.should_be_success_message()  # Проверяем, что сообщение о добавлении товара присутствует, и название товара совпадает
        page.should_be_basket_total_correct() # Проверяем, что итоговая стоимость корзины совпадает с ценой товара