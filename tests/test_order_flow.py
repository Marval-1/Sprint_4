import pytest
import allure
from pages.scooter_order_status_page import ScooterOrderStatusPage
from pages.scooter_order_rent_page import ScooterOrderRentPage
from pages.scooter_main_page import ScooterMainPage
from test_data import UserData
from test_data import Urls


@allure.story('TestOrderFlow')
class TestOrderFlow:
    @allure.feature('test order by using button from the header')
    @pytest.mark.parametrize('name, lastname, address, metro, phone', [
        UserData.Ivan,
        UserData.Nina
    ])
    def test_order_by_button_header(self, driver, form_by_header_order_button, name, lastname, address, metro, phone):
        form_by_header_order_button.filling_out_the_name_form(name, lastname, address, metro, phone)
        scooter_order_rent_page = ScooterOrderRentPage(driver)
        scooter_order_rent_page.filling_out_the_rent_form()
        text = scooter_order_rent_page.confirm_order()
        scooter_order_rent_page.click_button_order_status()
        assert 'Заказ оформлен' in text

    @allure.feature('test order by using button from the middle')
    @pytest.mark.parametrize('name, lastname, address, metro, phone', [
        UserData.Ivan,
        UserData.Nina
    ])
    def test_order_by_button_middle(self, driver, form_by_middle_order_button, name, lastname, address, metro, phone):
        form_by_middle_order_button.filling_out_the_name_form(name, lastname, address, metro, phone)
        scooter_order_rent_page = ScooterOrderRentPage(driver)
        scooter_order_rent_page.filling_out_the_rent_form()
        text = scooter_order_rent_page.confirm_order()
        scooter_order_rent_page.click_button_order_status()
        assert 'Заказ оформлен' in text

    @allure.feature('test click on logo from order status page')
    @pytest.mark.parametrize('name, lastname, address, metro, phone', [
        UserData.Ivan,
        UserData.Nina
    ])
    def test_click_on_logo_from_order_status_page(
            self, driver, form_by_middle_order_button, name, lastname, address, metro, phone):
        form_by_middle_order_button.filling_out_the_name_form(name, lastname, address, metro, phone)
        scooter_order_rent_page = ScooterOrderRentPage(driver)
        scooter_order_rent_page.filling_out_the_rent_form()
        scooter_order_rent_page.confirm_order()
        scooter_order_rent_page.click_button_order_status()

        scooter_order_status_page = ScooterOrderStatusPage(driver)
        scooter_order_status_page.click_logo_scooter()

        scooter_main_page = ScooterMainPage(driver)
        title = scooter_main_page.get_main_title()
        assert 'Самокат' in title

        scooter_order_status_page.click_logo_yandex(driver)
        scooter_order_status_page.switch_to_another_tab(driver)
        url = Urls()
        assert driver.current_url == url.yandex_url
