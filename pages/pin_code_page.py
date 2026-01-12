from pages.base_page import BasePage
from locators.pin_code_locators import PinCodeLocators


class PinCodePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def enter_pin_code(self, pin_code: str):
        for digit in pin_code:
            self.click(PinCodeLocators.digit(digit))

    def delete_pin_code(self):
        self.click(PinCodeLocators.BACKSPACE)

    def is_pin_title_visible(self) -> bool:
        elements = self.driver.find_elements(
            *PinCodeLocators.PIN_TITLE
        )
        return len(elements) > 0