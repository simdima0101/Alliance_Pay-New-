from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        self.find(locator, timeout).click()

    def is_element_present(self, locator, timeout=5):
        try:
            self.find(locator, timeout)
            return True
        except TimeoutException:
            return False

    def wait_until_not_visible(self, locator, timeout=10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
