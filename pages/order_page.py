import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу формы заказа")
    def fill_customer_info(self, data):
        self.enter_text(OrderPageLocators.NAME_INPUT, data["name"])
        self.enter_text(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, data["address"])

        self.click_element(OrderPageLocators.METRO_INPUT)
        self.enter_text(OrderPageLocators.METRO_INPUT, data["metro"])
        self.click_element(OrderPageLocators.metro_station_option(data["metro"]))

        self.enter_text(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click_element(OrderPageLocators.NEXT_BUTTON)


    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_rent_info(self, data):
        self.enter_text(OrderPageLocators.DATE_INPUT, data["date"])
        # Кликаем по заголовку "Про аренду", чтобы гарантированно закрыть календарь
        self.click_element(OrderPageLocators.RENT_HEADER)
        
        self.click_element(OrderPageLocators.PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.period_option(data["period"]))
        
        self.click_element(OrderPageLocators.color_checkbox(data["color"]))
        self.enter_text(OrderPageLocators.COMMENT_INPUT, data["comment"])
        self.click_element(OrderPageLocators.ORDER_SUBMIT_BUTTON)

    @allure.step("Подтвердить создание заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить отображение окна успешного заказа")
    def is_order_success_displayed(self):
        text = self.get_element_text(OrderPageLocators.ORDER_SUCCESS_HEADER)
        return "Заказ оформлен" in text

    