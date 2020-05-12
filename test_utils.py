from utils import *
import re

def test_generate_today_text():
    expected = re.compile(r'\d\d/\d\d（[月火水木金土日]）') #ex) 05/12（火）
    # given
    # when
    actual = generate_today_text()
    # then
    assert(expected.match(actual))

# TODO: I think should change itself to a slightly more testable method
def test_verify_options_help():
    expected = ([], False) 
    # given
    param = '--help'
    # when
    actual = verify_options(param)
    # then
    assert(actual == expected)

