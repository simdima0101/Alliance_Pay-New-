from appium.webdriver.common.appiumby import AppiumBy


class PinCodeLocators:
    
    @staticmethod
    def digit(digit: str):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{digit}")'
        )

    BACKSPACE = (AppiumBy.ACCESSIBILITY_ID, "Backspace")

    PIN_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Введите PIN-код")')