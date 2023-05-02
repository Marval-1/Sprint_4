import pytest
from selenium import webdriver

from pages.scooter_main_page import ScooterMainPage
from pages.scooter_main_page import LocatorScooterMainPage
from pages.scooter_order_name_page import ScooterOrderNamePage
from pages.scooter_order_name_page import LocatorOrderNamePage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(executable_path='./geckodriver') # На моей машине работает, если так прописан путь
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def initiation(driver):
    scooter_main_page = ScooterMainPage(driver)
    scooter_main_page.go_to_site(driver)
    scooter_main_page.accept_cookie()
    questions_all = scooter_main_page.find_element(LocatorScooterMainPage.questions_all, time=3)
    scooter_main_page.scroll_down(questions_all)

    return scooter_main_page


@pytest.fixture
def form_by_header_order_button(driver):
    scooter_order_name_page = ScooterOrderNamePage(driver)
    scooter_order_name_page.go_to_site(driver)
    scooter_order_name_page.click_button_order_header()

    return scooter_order_name_page


@pytest.fixture
def form_by_middle_order_button(driver):
    scooter_order_name_page = ScooterOrderNamePage(driver)
    scooter_order_name_page.go_to_site(driver)
    button = scooter_order_name_page.find_element(LocatorOrderNamePage.button_order_middle, time=3)
    scooter_order_name_page.scroll_down(button)
    scooter_order_name_page.click_button_order_middle()

    return scooter_order_name_page
