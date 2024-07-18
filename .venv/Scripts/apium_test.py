from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "emulator-5554",
    "appPackage": "com.example.eraspace",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver, 10)

def test_login_invalid():
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/username").send_keys("abcd")
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/password").send_keys("1234565")
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/login").click()

    error_message = wait.until(EC.presence_of_element_located((MobileBy.ID, "com.example.eraspace:id/error")))
    assert error_message.text == "Login gagal", "Expected error message not displayed"

def test_login_valid():
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/username").send_keys("085776461050")
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/password").send_keys("Astonm-13")
    driver.find_element(MobileBy.ID, "com.example.eraspace:id/login").click()

    home_page = wait.until(EC.presence_of_element_located((MobileBy.ID, "com.example.eraspace:id/home")))
    assert home_page.is_displayed(), "Home page not displayed after login"

    account_name = driver.find_element(MobileBy.ID, "com.example.eraspace:id/account_name")
    assert account_name.is_displayed(), "Account name not displayed"
    list_point = driver.find_element(MobileBy.ID, "com.example.eraspace:id/list_point")
    assert list_point.is_displayed(), "List point not displayed"

if __name__ == "__main__":
    test_login_invalid()
    test_login_valid()
    driver.quit()
