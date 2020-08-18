from import_proxy import *
import re
import os

def test_find_day_closed():
    expected = 14
    # given
    opts, headless = utils.verify_options('')
    driver = set_driver(headless)
    driver.get("file:///" + os.path.abspath("./test_data/records.htm"))
    time.sleep(0.5)
    # when
    actual = find_day_closed(driver)
    # then
    assert(actual == expected)
