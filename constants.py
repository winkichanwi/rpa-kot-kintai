# coding=utf-8

WEEKDAY_TXTS = {
    "0": "日",
    "1": "月",
    "2": "火",
    "3": "水",
    "4": "木",
    "5": "金",
    "6": "土"
}

USAGE = """usage:
   auto-kintai.py [-m <message>]
   auto-kintai.py [-s <HH:MM> | --start <HH:MM>] [-e <HH:MM> | --end <HH:MM>] [--headless]
   auto-kintai.py -h | --help

options:
   -h, --help                      Show usage.
   -s <HH:MM>, --start <HH:MM>     Apply start of work record in 24-hour format.
   -e <HH:MM>, --end <HH:MM>       Apply end of work record in 24-hour format.
   --headless                      Run Chrome in headless mode.
   -m <message>                    Apply record with message.

When option is not provided, timesheet record will be applied in current time.
"""
