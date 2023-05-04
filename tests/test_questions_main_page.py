import pytest
import allure
from pages.scooter_main_page import ScooterMainPage

from test_data import SectionQuestions


@allure.title('TestQuestions')
class TestQuestions:

    @allure.feature('Test of answers to all questions')
    @pytest.mark.parametrize('question_locator, answer_locator, text', SectionQuestions.data)
    def test_question_common(self, driver, initiation, question_locator, answer_locator, text):
        initiation.click_question_element(question_locator)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(answer_locator)

        assert dropdown_text == text
