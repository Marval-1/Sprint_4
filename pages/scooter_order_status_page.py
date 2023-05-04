import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LocatorOrderStatusPage:
    logo_yandex = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    logo_scooter = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]
    button_order_status = [By.XPATH, ".//button[contains(text(), 'Посмотреть статус')]"]
    dzen_title = [By.XPATH, "/html/head/title"]


class ScooterOrderStatusPage(BasePage):
    @allure.step('click on logo yandex')
    def click_logo_yandex(self, driver):
        logo_yandex = self.find_element(LocatorOrderStatusPage.logo_yandex, time=3)
        logo_yandex.click()

    @allure.step('click on logo scooter')
    def click_logo_scooter(self):
        logo_scooter = self.find_element(LocatorOrderStatusPage.logo_scooter, time=3)
        logo_scooter.click()
        