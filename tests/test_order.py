import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import ORDER_DATA_1, ORDER_DATA_2


class TestOrder:
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize(
        "order_button, user_data",
        [
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_2),
        ],
    )
    def test_create_order_success(self, driver, order_button, user_data):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.fill_customer_info(user_data)
        order_page.fill_rent_info(user_data)
        order_page.confirm_order()

        assert order_page.is_order_success_displayed()
