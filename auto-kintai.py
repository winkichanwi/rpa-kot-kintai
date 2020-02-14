import sys, getopt, time
import utils
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def read_input():
    employeeId = input("Enter username: wtv3")
    username = "wtv3" + employeeId
    password = getpass("Enter password: ")
    return (username, password)

def setup():
    # driverOpt = webdriver.ChromeOptions()
    # driverOpt.headless = True
    # driver = webdriver.Chrome(options = driverOpt)
    driver = webdriver.Chrome()
    return driver

def login(driver, username, password):
    driver.get("https://s2.kingtime.jp/admin")
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

### Open form
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

def findOpenTimesheetFormButtonIndex(todayButtonOptions):
    optionTexts = []
    for op in todayButtonOptions:
        optionTexts.append(op.text)
    return optionTexts.index("打刻申請")

def openTimesheetForm(driver):
    # assert timesheet page
    time.sleep(0.5)
    timesheetPage = driver.find_element_by_class_name("htBlock-adjastableTableF_inner")
    print("Logged in to King of Time")

    todayRowIndex = findTodayRowIndex(driver)
    todayButton = driver.find_elements_by_class_name("htBlock-selectOther")[todayRowIndex]
    todayButtonOptions = todayButton.find_elements_by_tag_name("option")
    openFormOptionIndex = findOpenTimesheetFormButtonIndex(todayButtonOptions)
    openFormButton = todayButtonOptions[openFormOptionIndex]
    openFormButton.click()
    return

### Enter timesheet
def isStartOfWorkApplied(driver):
    # TODO: define hasPendingApplication more accurately by history content
    hasPendingApplication = False
    try:
        hasPendingApplication = driver.find_element_by_class_name("specific-table_1000_wrap")
    except NoSuchElementException:
        hasPendingApplication = False

    isStartOfWorkEntered = False
    recordTypeMenus = driver.find_elements_by_class_name("htBlock-selectmenu")
    recordTypeOptions = []
    for m in recordTypeMenus:
        try:
            recordTypeOptions.append(m.find_elements_by_css_selector("option:selected"))
        except NoSuchElementException:
            continue
    if len(recordTypeOptions) > 0:
        for opt in recordTypeOptions:
            isStartOfWorkEntered = (opt.text == "出勤") or isStartOfWorkEntered

    return hasPendingApplication or isStartOfWorkEntered

def enterTimesheet(driver, opts, args):
    # assert timesheet form
    time.sleep(0.5)
    timesheetForm = driver.find_elements_by_id("recording_timestamp_table")

    if len(opts) == 0:
        # TODO: enter current time
        shouldEnterStartOfWork = not(isStartOfWorkApplied(driver))
            ## yes: enter end
            ## no: enter start
    # TODO: enter start time
    # TODO: enter end time
    return

### Main
def main(argv):
    # print help
    try:
      opts, args = getopt.getopt(argv,"h",["help"])
    except getopt.GetoptError:
        print("usage: auto-kintai.py [-s HH:mm | -e HH:mm]")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("usage: auto-kintai.py [-s HH:mm | -e HH:mm]")
            sys.exit(2)
            
    username, password = read_input()
    driver = setup()
    login(driver, username, password)
    openTimesheetForm(driver)
    enterTimesheet(driver, opts, args)
    time.sleep(1)
    driver.close()

if __name__ == "__main__":
    main(sys.argv[1:])
