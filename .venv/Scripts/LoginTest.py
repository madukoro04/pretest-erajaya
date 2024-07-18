from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def test_login_invalid_data():
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID, "btn-make-appointment").click()

    driver.find_element(By.ID, "txt-username").send_keys("adrian")
    print("Data berhasil terinput")
    driver.find_element(By.ID, "txt-password").send_keys("123456")
    print("Data berhasil terinput")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-login"))).click()
    time.sleep(3)
    assert "Login failed! Please ensure the username and password are valid." in driver.page_source

def test_login_valid_data():
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID, "btn-make-appointment").click()

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    print("Data berhasil terinput")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    print("Data berhasil terinput")
    driver.find_element(By.ID, "btn-login").click()

    time.sleep(3)
    assert "https://katalon-demo-cura.herokuapp.com/#appointment" in driver.current_url
    driver.get("https://katalon-demo-cura.herokuapp.com")


try:
    test_login_invalid_data()
    print("TC 1.1 Login gagal dan tampil pesan error")
except AssertionError:
    print("TC 1.1 Test Case Gagal")

try:
    test_login_valid_data()
    print("TC 1.2 Login success")
    print("Redirect ke homepage (Make appointment)")
except AssertionError:
    print("TC 1.2 Test Case Gagal")

time.sleep(10)

driver.quit()
