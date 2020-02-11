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
```
$ python auto-kintai.py
```
usernameは先頭に `wtv3` を付いていると想定され、社員番号を入力するだけ
