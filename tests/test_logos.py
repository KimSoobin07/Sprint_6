import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


class TestLogos:
    @allure.title("Переход на главную страницу при клике на логотип 'Самокат'")
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_TOP)
        main_page.click_scooter_logo()
        assert driver.current_url == BASE_URL

    @allure.title("Открытие главной страницы Дзена в новом окне при клике на логотип 'Яндекс'")
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url_not_about_blank()
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex.ru" in current_url

