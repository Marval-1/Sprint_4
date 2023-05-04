import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorOrderRentPage:
    input_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    dropdown_rental_time = [By.XPATH, ".//div[@class='Dropdown-control']"]
    button_rental_time = [By.XPATH, ".//div[contains(text(), 'двое суток')]"]
    button_calendar = [By.XPATH, ".//div[@aria-label='Choose вторник, 30-е мая 2023 г.']"]
    button_order_final = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    modal_window_order_title = [By.XPATH, ".//div[contains(text(), 'Хотите оформить заказ?')]"]
    modal_window_order_success_title = [By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]"]
    button_YES = [By.XPATH, ".//button[contains(text(), 'Да')]"]
    button_order_status = [By.XPATH, ".//button[contains(text(), 'Посмотреть статус')]"]


class ScooterOrderRentPage(BasePage):
    @allure.step('filling out the rent form')
    def filling_out_the_rent_form(self):
        input_date = self.find_element(LocatorOrderRentPage.input_date, time=3)
        input_date.send_keys('30.05.2023')
        button_calendar = self.find_element(LocatorOrderRentPage.button_calendar, time=3)
        button_calendar.click()

        dropdown_rental_time = self.find_element(LocatorOrderRentPage.dropdown_rental_time, time=3)
        dropdown_rental_time.click()
        button_rental_time = self.find_element(LocatorOrderRentPage.button_rental_time, time=3)
        button_rental_time.click()

        button_order_final = self.find_element(LocatorOrderRentPage.button_order_final, time=3)
        button_order_final.click()

    @allure.step('confirm order')
    def confirm_order(self):
        button_yes = self.find_element(LocatorOrderRentPage.button_YES, time=3)
        button_yes.click()
        modal_window_order_success_title = self.find_element(LocatorOrderRentPage.modal_window_order_success_title, time=3)
        return modal_window_order_success_title.text

    @allure.step('click order status button')
    def click_button_order_status(self):
        button_order_status = self.find_element(LocatorOrderRentPage.button_order_status, time=3)
        button_order_status.click()
