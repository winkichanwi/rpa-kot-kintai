from datetime import date

def generateTodayText():
    today = date.today()
    dateText = today.strftime("%m/%d")
    weekdayNum = today.strftime("%w")
    weekdayDic = {
      "0": "日",
      "1": "月",
      "2": "火",
      "3": "水",
      "4": "木",
      "5": "金",
      "6": "土"
    }
    return dateText + "（" + weekdayDic[weekdayNum] + "）"
