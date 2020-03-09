# coding=utf-8
import sys, time
from datetime import datetime
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import utils, constants
from enums import RecordType

def read_input():
    employee_id = input("Enter username: wtv3")
    username = "wtv3" + employee_id
    password = getpass("Enter password: ")
    return (username, password)

def setup(headless):
    driverOpt = webdriver.ChromeOptions()
    driverOpt.headless = headless
    driver = webdriver.Chrome(options = driverOpt)
    return driver

def login(driver, username, password):
    driver.get("https://s2.kingtime.jp/admin")
    # assert login page
    login_form = driver.find_element_by_class_name("specific-loginForm")

    # login
    username_input = driver.find_element_by_id("login_id")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element_by_id("login_password")
    password_input.clear()
    password_input.send_keys(password)

    login_button = driver.find_element_by_id("login_button")
    login_button.click()
    return

### Open form
def find_today_row_index(day_rows):
    day_texts = []
    for r in day_rows:
        day_texts.append(r.find_element_by_tag_name("p").text)
    today_text = utils.generate_today_text()
    return day_texts.index(today_text)

def find_open_timesheet_form_button_index(today_button_option_elements):
    option_texts = []
    for op in today_button_option_elements:
        option_texts.append(op.text)
    return option_texts.index("打刻申請")

def open_timesheet_form(driver):
    # assert timesheet page
    time.sleep(0.5)
    timesheet_page = driver.find_element_by_class_name("htBlock-adjastableTableF_inner")
    print("Logged in to King of Time.")

    day_rows = driver.find_elements_by_class_name("htBlock-scrollTable_day")
    today_row_index = find_today_row_index(day_rows)
    today_button = driver.find_elements_by_class_name("htBlock-selectOther")[today_row_index]
    today_button_option_elements = today_button.find_elements_by_tag_name("option")
    timesheet_form_option_index = find_open_timesheet_form_button_index(today_button_option_elements)
    timesheet_form_button = today_button_option_elements[timesheet_form_option_index]
    timesheet_form_button.click()
    return

### Enter timesheet
def is_application_pending(driver, record_type):
    has_pending_application = False
    pending_application_table = driver.find_elements_by_class_name("specific-table_1000_wrap")
    if len(pending_application_table) > 0:
        pending_record_elements = pending_application_table[0].find_elements_by_tag_name("td")
        for e in pending_record_elements:
            has_pending_application = (record_type.value in e.text) or has_pending_application
    else:
        has_pending_application = False
    return has_pending_application

def find_selected_record_type_option_elements(record_type_menu_elements):
    record_type_option_elements = []
    for m in record_type_menu_elements:
        select = Select(m)
        record_type_option_elements = record_type_option_elements + select.all_selected_options
    return record_type_option_elements

def is_specific_record_type_selected(record_type_menu_elements, record_type):
    is_record_type_selected = False
    selected_option_elements = find_selected_record_type_option_elements(record_type_menu_elements)
    if len(selected_option_elements) > 0:
        for opt in selected_option_elements:
            is_record_type_selected = (opt.text == record_type.value) or is_record_type_selected
    return is_record_type_selected

def is_specific_record_type_applied(driver, record_type_menu_elements, record_type):
    has_pending_application = is_application_pending(driver, record_type)
    is_record_type_selected = is_specific_record_type_selected(record_type_menu_elements, record_type)
    return has_pending_application or is_record_type_selected

def enter_records(driver, record_type_menu_elements, records):
    available_row_index = []
    record_type_select_elements = []
    for i in range(len(record_type_menu_elements)):
        select = Select(record_type_menu_elements[i])
        record_type_select_elements.append(select)
        if select.first_selected_option.text == " --選択してください-- ":
            available_row_index.append(i)
    time_input_elements = driver.find_elements_by_class_name("recording_timestamp_time")
    i = 0
    for record_type, time_text in records.items():
        row_index = available_row_index[i]
        # select record type
        record_type_select_elements[row_index].select_by_visible_text(record_type.value)
        # input time
        time_input_elements[row_index].send_keys(time_text)
        print("Entered " + record_type.value + " at " + time_text)
        i += 1
    return

def enter_timesheet(driver, opts):
    # assert timesheet form
    time.sleep(0.5)
    timesheet_form = driver.find_elements_by_id("recording_timestamp_table")

    record_type_menu_elements = driver.find_elements_by_class_name("htBlock-selectmenu")
    should_enter_start_of_work = not(is_specific_record_type_applied(driver, record_type_menu_elements, RecordType.START_OF_WORK))
    should_enter_end_of_work = not(is_specific_record_type_applied(driver, record_type_menu_elements, RecordType.END_OF_WORK))

    input_records = {}
    should_enter_current_time = True
    for opt, arg in opts:
        if opt in ("-s", "--start"):
            should_enter_current_time = False
            # enter start of work
            if should_enter_start_of_work:
                input_records[RecordType.START_OF_WORK] = arg
            else:
                print("Start of work is applied already.")
        elif opt in ("-e", "--end"):
            should_enter_current_time = False
            # enter end of work
            if should_enter_end_of_work:
                input_records[RecordType.END_OF_WORK] = arg
            else:
                print("End of work is applied already.")
    if should_enter_current_time:
        # enter current time
        current_time_text = datetime.now().strftime("%H:%M")
        if should_enter_start_of_work:
            input_records[RecordType.START_OF_WORK] = current_time_text
        elif should_enter_end_of_work:
            input_records[RecordType.END_OF_WORK] = current_time_text
        else:
            print("Today's timesheet is applied already.")
    if len(input_records) > 0:
        enter_records(driver, record_type_menu_elements, input_records)
    # submit
    submit_button = driver.find_element_by_class_name("htBlock-buttonSave")
    submit_button.click()
    return

### Main
def main(argv):
    opts, args, headless = utils.verify_options(argv)
    username, password = read_input()
    driver = setup(headless)
    try:
        login(driver, username, password)
        open_timesheet_form(driver)
        enter_timesheet(driver, opts)
    except NoSuchElementException as e:
        print("Element not found.\nUI may be changed, please modify code according to the change.\n", e)
    except:
        print("Unexpected error.\n", sys.exc_info()[1])
    else:
        print("Complete timesheet application.")
        if not(headless):
            time.sleep(5)
    finally:
        driver.close()

if __name__ == "__main__":
    main(sys.argv[1:])
