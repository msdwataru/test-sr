## Set up
### Youtube Data APIの有効化とAPI Keyを取得する
https://developers.google.com/youtube/v3/quickstart/python

### 環境変数設定
```
cp .env.sample .env
```
上で取得したAPI_KEYを設定

### pythonライブラリインストール
```
pipenv sync
```

## 実行
### ans1
```
pipenv run python ans1.py --num_fetched 100
```

### ans2
```
pipenv run python ans2.py --num_fetched 10
```