import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LocatorScooterMainPage:
    cookie_button = [By.XPATH, "//button[@id='rcc-confirm-button']"]
    questions_all = [By.XPATH, "//div[contains(text(), 'Вопросы о важном')]"]
    question_price = [By.ID, 'accordion__heading-0']
    dropdown_price = [By.ID, 'accordion__panel-0']
    question_several = [By.ID, 'accordion__heading-1']
    dropdown_several = [By.ID, 'accordion__panel-1']
    question_rental_time = [By.ID, 'accordion__heading-2']
    dropdown_rental_time = [By.ID, 'accordion__panel-2']
    question_rented_today = [By.ID, 'accordion__heading-3']
    dropdown_rented_today = [By.ID, 'accordion__panel-3']
    question_extend_the_order = [By.ID, 'accordion__heading-4']
    dropdown_extend_the_order = [By.ID, 'accordion__panel-4']
    question_charger = [By.ID, 'accordion__heading-5']
    dropdown_charger = [By.ID, 'accordion__panel-5']
    question_cancel_the_order = [By.ID, 'accordion__heading-6']
    dropdown_cancel_the_order = [By.ID, 'accordion__panel-6']
    question_beyond_the_MKAD = [By.ID, 'accordion__heading-7']
    dropdown_beyond_the_MKAD = [By.ID, 'accordion__panel-7']
    main_title = [By.XPATH, ".//div[@class='Home_Header__iJKdX']"]


class ScooterMainPage(BasePage):

    @allure.step('accept cookie')
    def accept_cookie(self):
        cookie_button = self.find_element(LocatorScooterMainPage.cookie_button, time=3)
        cookie_button.click()

    def click_question_element(self, locator):
        question_title = self.find_element(locator, time=3)
        question_title.click()

    def get_dropdown_text(self, locator):
        dropdown = self.find_element(locator, time=3)
        return dropdown.text

    def get_main_title(self):
        main_title = self.find_element(LocatorScooterMainPage.main_title, time=3)
        return main_title.text
