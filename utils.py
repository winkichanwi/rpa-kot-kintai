import sys, getopt
from datetime import datetime

import constants

def generate_today_text():
    now = datetime.now()
    dateText = now.strftime("%m/%d")
    weekdayNum = now.strftime("%w")
    return dateText + "（" + constants.WEEKDAY_TXTS[weekdayNum] + "）"

def verify_options(argv):
    headless = False
    try:
      opts, args = getopt.getopt(argv,"hs:e:",["help","headless","start=","end="])
    except getopt.GetoptError:
        print(constants.USAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(constants.USAGE)
            sys.exit(0)
        elif opt in ("--headless"):
            headless = True
        elif opt in ("-s", "-e", "--start", "--end"):
            try:
                input_time = datetime.strptime(arg, "%H:%M")
            except ValueError:
                print("Wrong time format. Please see usage.\n")
                print(constants.USAGE)
                sys.exit(2)
    return (opts, headless)
