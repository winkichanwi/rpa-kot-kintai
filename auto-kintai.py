import utils
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
    return

def findTodayRowIndex(driver):
    dayRows = driver.find_elements_by_class_name("htBlock-scrollTable_day")
    dayElements = []
    for r in dayRows:
        dayElements.append(r.find_element_by_tag_name("p"))
    dayTexts = []
    for p in dayElements:
        dayTexts.append(p.text)
    todayText = utils.generateTodayText()
    return dayTexts.index(todayText)

def findOpenAttendanceFormButtonIndex(todayButtonOptions):
    optionTexts = []
    for op in todayButtonOptions:
        optionTexts.append(op.text)
    return optionTexts.index("打刻申請")

def openAttendanceForm(driver):
    # assert main page
    time.sleep(0.5)
    mainPage = driver.find_element_by_class_name("htBlock-adjastableTableF_inner")

    # TODO: find today's row
    todayRowIndex = findTodayRowIndex(driver)
    todayButton = driver.find_elements_by_class_name("htBlock-selectOther")[todayRowIndex]
    todayButtonOptions = todayButton.find_elements_by_tag_name("option")
    openFormOptionIndex = findOpenAttendanceFormButtonIndex(todayButtonOptions)
    openFormButton = todayButtonOptions[openFormOptionIndex]
    openFormButton.click()
    return

def enterAttendance(driver):
    # TODO: assert attendence form #recording_timestamp_table
    time.sleep(0.5)
    # TODO: enter start time
    # TODO: enter end time
    return

def main():
    username, password = read_input()
    driver = setup()
    login(driver, username, password)
    openAttendanceForm(driver)
    enterAttendance(driver)
    time.sleep(1)
    driver.close()

if __name__ == "__main__":
    main()
