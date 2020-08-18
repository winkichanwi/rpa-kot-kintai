# README
King of Time の打刻入力をCLIから実行するための
Pythonスクリプトです

## 環境構築
1. Python (^3.6) with pip / Google Chrome

2. Install Libraries
```
$ pip install -r requirements.txt --user

# 以下のエラーが出たらこっちで
#WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl
#ERROR: Could not install packages due to an EnvironmentError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)')))
$ pip install -r requirements.txt --user --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

```

## パスワードを保存したい人

`.env.sample` をコピーして `.env` ファイルを作成します、
King of Time にログインする際のパスワードとIDを保存してください

```.env
USERNAME=wtv3001234
PASSWORD=abc123
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

`.env` を指定していない場合、実行の際に `username` と `password` が聞かれます
`username` は先頭に `wtv3` を付いていることと想定され、社員番号を入力するだけでOK

他のユースケースの実行方法は `--help` で参考してください


## unit test

```
❯ pytest -v
====================================================== test session starts =======================================================
platform darwin -- Python 3.8.2, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/xx/.pyenv/versions/3.8.2/bin/python3
cachedir: .pytest_cache
rootdir: /Users/xx/work/rpa-kot-kintai
collected 2 items

test_utils.py::test_generate_today_text PASSED                                                                             [ 50%]
test_utils.py::test_verify_options_help PASSED                                                                             [100%]
```

## troubleshooting
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX
```
requirements.txt/chromedriver-binary とローカルのGoogle Chromeのバージョンをあわせる必要があります
https://pypi.org/project/chromedriver-binary/#history
