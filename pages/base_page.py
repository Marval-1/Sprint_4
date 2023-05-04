import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LocatorYandexTab:
    ya_input_search = [By.XPATH, ".//div[@class='dzen-desktop__search-37']"]


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('go to site')
    def go_to_site(self, driver):
        return self.driver.get(self.base_url)

    @allure.step('find element')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not found {locator}')

    @allure.step('scroll down')
    def scroll_down(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @allure.step('switch to second tab')
    def switch_to_another_tab(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorYandexTab.ya_input_search))
        new_url = driver.current_url
        return new_url
