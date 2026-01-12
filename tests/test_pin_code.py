from pages.pin_code_page import PinCodePage
from locators.pin_code_locators import PinCodeLocators
import pytest

def test_enter_pin_code(driver):
    pin_code_page = PinCodePage(driver)

    #enter pin code
    pin_code_page.enter_pin_code("1222")

    assert pin_code_page.wait_until_not_visible(PinCodeLocators.PIN_TITLE), (
        "Экран PIN-кода не исчез после ввода"
    )
