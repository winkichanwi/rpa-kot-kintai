import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def read_input():
    employeeId = input("Enter username: wtv3")
    username = "wtv3" + employeeId
    password = getpass("Enter password: ")
    return (username, password)

def setup():
    driver = webdriver.Chrome()
    return driver

def login(driver, username, password):
    driver.get("https://s2.kingtime.jp/admin")
    assert "KING OF TIME" in driver.title
    # assert login page
    loginForm = driver.find_element_by_class_name("specific-loginForm")

    # login
    usernameField = driver.find_element_by_id("login_id")
    usernameField.clear()
    usernameField.send_keys(username)

    passwordField = driver.find_element_by_id("login_password")
    passwordField.clear()
    passwordField.send_keys(password)

    passwordField.send_keys(Keys.RETURN)

def openAttendanceForm(driver):
    # assert main page
    mainPage = driver.find_element_by_class_name("htBlock-adjastableTableF_inner")
    # TODO: find today's row
    # rows of day .htBlock-scrollTable_day -> find p .text
    return

# TODO: assert attendence form #recording_timestamp_table

def main():
    username, password = read_input()
    driver = setup()
    login(driver, username, password)
    openAttendanceForm(driver)
    time.sleep(10)
    driver.close()

main()
