from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def login():
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-make-appointment"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txt-username"))).send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()


def test_make_appointment_without_date():
    login()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "combo_facility"))).click()
    driver.find_element(By.ID, "combo_facility").send_keys("Tokyo CURA Healthcare Center")
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()
    print("Tanggal Kosong")
    driver.find_element(By.ID, "txt_comment").send_keys("Test Case 2.1")
    print("Data berhasil terinput")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-book-appointment"))).click()
    time.sleep(3)
    assert "Please fill out this field." in driver.page_source

def test_make_appointment_success():
    driver.refresh()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "combo_facility")))
    driver.find_element(By.ID, "combo_facility").send_keys("Hongkong CURA Healthcare Center ")
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys("18/07/2024")
    driver.find_element(By.ID, "txt_comment").send_keys("Test Case 2.2")
    print("Data berhasil terinput")

    driver.find_element(By.ID, "btn-book-appointment").click()
    time.sleep(3)
    assert "Appointment Confirmation" in driver.page_source


try:
    test_make_appointment_without_date()
    print("TC 2.1 Berhasil Menampilkan error message, mandatory field harus diiisi")
except AssertionError:
    print("TC 2.1 Gagal")

try:
    test_make_appointment_success()
    print("TC 2.2 Berhasil")
    print("Berhasil membuat appointment dan menampilkan data appointment yang sudah diinput sebelumnya")
except AssertionError:
    print("TC 2.2 Gagal")

time.sleep(10)
driver.quit()
