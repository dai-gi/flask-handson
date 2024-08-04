# flask-handson

## セットアップ
### リポジトリクローン
```shell
git clone git@github.com:dai-gi/flask-handson.git
cd flask-handson
```

### 仮想環境構築
```shell
python3 -m venv venv
. venv/bin/activate
```

### ライブラリインストール
```shell
pip install --upgrade pip
pip install -r requirements.txt
```

### データベース初期化
```shell
flask --app app init-db
```

### アプリケーション実行
```shell
flask --app app run
```
