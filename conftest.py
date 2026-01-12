import pytest
from appium import webdriver
from config.driver_config import android_options

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=android_options()
    )

    # Гарантированный запуск приложения
    driver.activate_app("uz.tune.juicer")

    yield driver

    driver.terminate_app("uz.tune.juicer")
    driver.quit()