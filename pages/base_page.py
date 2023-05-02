import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self, driver):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not found {locator}')

    def scroll_down(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)
        time.sleep(1)

    def switch_to_another_tab(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        new_url = driver.current_url
        return new_url
