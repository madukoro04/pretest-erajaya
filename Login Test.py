from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()


# Test Case 1.1: Login with invalid data
def test_login_invalid_data():
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on the 'Make Appointment' button
    driver.find_element(By.ID, "btn-make-appointment").click()

    # Input invalid username and valid password
    driver.find_element(By.ID, "txt-username").send_keys("invalidUser")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    # Validate error message is displayed
    error_message = driver.find_element(By.CLASS_NAME, "lead text-danger").text
    assert "Login failed! Please ensure the username and password are valid." in error_message


# Test Case 1.2: Login with valid data
def test_login_valid_data():
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on the 'Make Appointment' button
    driver.find_element(By.ID, "btn-make-appointment").click()

    # Input valid username and valid password
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    # Validate redirection to homepage
    time.sleep(3)  # Wait for the page to load
    assert "https://katalon-demo-cura.herokuapp.com/#appointment" in driver.current_url


# Execute tests
try:
    test_login_invalid_data()
    print("Test Case 1.1 Passed")
except AssertionError:
    print("Test Case 1.1 Failed")

try:
    test_login_valid_data()
    print("Test Case 1.2 Passed")
except AssertionError:
    print("Test Case 1.2 Failed")

# Close the WebDriver
driver.quit()
