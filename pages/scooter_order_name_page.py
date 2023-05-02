from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LocatorOrderNamePage:
    button_order_header = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(), 'Заказать')]"]
    button_order_middle = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]"]
    input_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_lastname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    input_phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_NEXT = [By.XPATH, ".//button[contains(text(), 'Далее')]"]


class ScooterOrderNamePage(BasePage):

    def click_button_order_header(self):
        button_order_header = self.find_element(LocatorOrderNamePage.button_order_header, time=3)
        button_order_header.click()

    def click_button_order_middle(self):

        button_order_middle = self.find_element(LocatorOrderNamePage.button_order_middle, time=3)
        self.scroll_down(button_order_middle)
        button_order_middle.click()

    def filling_out_the_name_form(self, name, lastname, address, metro, phone):
        input_name = self.find_element(LocatorOrderNamePage.input_name, time=3)
        input_name.send_keys(name)

        input_lastname = self.find_element(LocatorOrderNamePage.input_lastname, time=3)
        input_lastname.send_keys(lastname)

        input_address = self.find_element(LocatorOrderNamePage.input_address, time=3)
        input_address.send_keys(address)

        input_metro = self.find_element(LocatorOrderNamePage.input_metro, time=3)
        input_metro.send_keys(metro)
        input_metro.send_keys(Keys.DOWN)
        input_metro.send_keys(Keys.ENTER)

        input_phone = self.find_element(LocatorOrderNamePage.input_phone, time=3)
        input_phone.send_keys(phone)

        button_next = self.find_element(LocatorOrderNamePage.button_NEXT, time=3)
        button_next.click()
