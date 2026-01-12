from appium.options.android import UiAutomator2Options


def android_options():
    options = UiAutomator2Options()

    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")

    options.set_capability("deviceName", "Android Device")

    options.set_capability("appPackage", "uz.tune.juicer")
    options.set_capability("appActivity", ".MainActivity")

    options.set_capability("noReset", True)

    return options