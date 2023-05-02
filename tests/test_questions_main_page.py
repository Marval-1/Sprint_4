from pages.scooter_main_page import ScooterMainPage
from pages.scooter_main_page import LocatorScooterMainPage
import allure
from test_data import MainPageQuestionsData


@allure.story('TestQuestions')
class TestQuestions:
    @allure.feature('Test answer about price')
    def test_question_price(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_price)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_price)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_price

    @allure.feature('Test answer about several')
    def test_question_several(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_several)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_several)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_several

    @allure.feature('Test answer about rental time')
    def test_question_rental_time(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_rental_time)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_rental_time)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_rental_time

    @allure.feature('Test answer about rented today')
    def test_question_rented_today(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_rented_today)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_rented_today)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_rented_today

    @allure.feature('Test answer about extend the order')
    def test_question_extend_the_order(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_extend_the_order)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_extend_the_order)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_extend_the_order

    @allure.feature('Test answer about charger')
    def test_question_charger(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_charger)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_charger)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_charger

    @allure.feature('Test answer about cancel the order')
    def test_question_cancel_the_order(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_cancel_the_order)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_cancel_the_order)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_cancel_the_order

    @allure.feature('Test answer about beyond MKAD')
    def test_question_beyond_the_mkad(self, driver, initiation):
        initiation.click_question_element(LocatorScooterMainPage.question_beyond_the_MKAD)

        scooter_main_page = ScooterMainPage(driver)
        dropdown_text = scooter_main_page.get_dropdown_text(LocatorScooterMainPage.dropdown_beyond_the_MKAD)

        main_page_questions_data = MainPageQuestionsData()
        assert dropdown_text == main_page_questions_data.data_dropdown_beyond_the_MKAD
