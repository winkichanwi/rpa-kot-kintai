# README

## 環境構築
1. Python (^3.6) with pip

2. selenium
```
pip install selenium
```

3. chromedriver

- ダウンロード: https://sites.google.com/a/chromium.org/chromedriver/downloads
- `chromedriver` を `PATH` (`/usr/bin` or `/usr/local/bin`) にコピーする

```
sudo cp ./chromedriver /usr/local/bin
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
