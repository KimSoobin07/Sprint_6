from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Страница 1: "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    @staticmethod
    def metro_station_option(station_name):
        return (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station_name}']")


    # Страница 2: "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    RENT_HEADER = (By.XPATH, "//div[text()='Про аренду']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Модальное окно подтверждения
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")

    @staticmethod
    def period_option(period_text):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period_text}']")

    @staticmethod
    def color_checkbox(color_id):
        return (By.ID, color_id)
