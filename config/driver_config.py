from appium.options.android import UiAutomator2Options


def android_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "Pixel 8 Pro"
    options.automation_name = "UiAutomator2"

    options.device_name = ""   # adb devices
    options.udid = ""

    options.app_package = "uz.tune.juicer"
    options.app_activity = "uz.tune.juicer.ui.activity.main.MainActivityDefault"
    options.app_wait_activity = "*"

    options.no_reset = True
    options.new_command_timeout = 300

    return options