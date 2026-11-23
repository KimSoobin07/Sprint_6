import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Закрыть баннер с куками")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Нажать на вопрос FAQ под индексом {index}")
    def click_faq_question(self, index):
        locator = MainPageLocators.faq_question(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить текст ответа FAQ под индексом {index}")
    def get_faq_answer_text(self, index):
        locator = MainPageLocators.faq_answer(index)
        return self.get_element_text(locator)

    @allure.step("Нажать кнопку 'Заказать' (точка входа)")
    def click_order_button(self, button_locator):
        self.scroll_to_element(button_locator)
        self.click_element(button_locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)
