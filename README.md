# README

## 環境構築
1. Python (^3.6) with pip / Google Chrome

2. Install Libraries
```
$ pip install -r requirements.txt
```

## 実行
1. 今の時間で打刻の場合（出勤か退勤かは履歴から判断する）
```
$ python auto-kintai.py
```

2. 指定の出勤時間の打刻の場合
```
$ python auto-kintai.py -s 09:30
```

3. 指定の退勤時間の打刻の場合 (Headless Chrome)
```
$ python auto-kintai.py -e 19:30 --headless
```

実行の際に `username` と `password` が聞かれます

`username` は先頭に `wtv3` を付いていることと想定され、社員番号を入力するだけでOK

他のユースケースの実行方法は `--help` で参考してください

## troubleshooting
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX
```
requirements.txt/chromedriver-binary とローカルのGoogle Chromeのバージョンをあわせる必要があります
https://pypi.org/project/chromedriver-binary/#history
