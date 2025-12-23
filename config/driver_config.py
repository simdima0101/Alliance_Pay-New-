from appium.options.android import UiAutomator2Options


def android_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"

    options.app_package = ""
    options.app_activity = ""

    options.no_reset = True

    return options