import pytest
import allure
from pages.main_page import MainPage
from data import FAQ_ANSWERS


class TestFaq:
    @allure.title("Проверка текста ответа в разделе 'Вопросы о важном' (вопрос №{index})")
    @pytest.mark.parametrize("index, expected_answer", FAQ_ANSWERS.items())
    def test_faq_question_opens_correct_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)
        assert actual_answer == expected_answer
