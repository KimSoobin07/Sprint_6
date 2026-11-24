from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка принятия кук (часто перекрывает нижние элементы)
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотипы в шапке
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Кнопки "Заказать" (вверху и внизу)
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    # Раздел FAQ (шаблоны локаторов для параметризации по индексу 0..7)
    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")
