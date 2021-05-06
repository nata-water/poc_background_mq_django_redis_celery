
## 非同期処理の検証

* フロントエンド + Django REST framework + Redis + Celeryで非同期処理
* 作業1
  * [x] Django REST framework(以下DRF)のエンドポイントからCelery関数が実行でき、DBに結果が書き込まれること
  * [x] Celery時間のかかる処理を試す
* 作業2
  * [x] Celery関数を実行後、DjangoモデルのBLOBを格納し、別モデルにデータを格納する
    * BinaryResourceモデル内のExcelデータ -> ParseResultの各行列に分割
  * [ ] [option]Celery関数終了後のブラウザへの通知方法の検討
  * [x] [option]フロント画面からの呼び出し
  * [ ] [option]同時アクセス時の負荷分散について調べる

## 使い方


### コンテナ起動

```sh
$ docker-compose up -d
```

### 事前準備1：必要なモジュールのインストール

```sh
$ cd backend
$ pip install pipenv
$ pipenv shell
# Pipfileを元にインストールするため、特にモジュール名の指定は不要
$ pipenv install
```

### 事前準備2：Djangoのマイグレーション実行とユーザ作成・開発サーバ起動

```sh
$ pipenv shell
$ python manage.py migrate
$ python manage.py createsuperuser --username admin --email admin@foobar.com --skip-checks
# [!] 以下のメッセージが表示されるため好きなパスワードを指定
# 　>Password: admin
# 　>Password (again):admin
# [!] パスワードの注意メッセージが表示されるが、yを指定すれば問題なし
# 　このパスワードは ユーザー名 と似すぎています。
# 　このパスワードは短すぎます。最低 8 文字以上必要です。
# 　このパスワードは一般的すぎます。
# 　Bypass password validation and create user anyway? [y/N]:
$ python manage.py loaddata xxx_api/fixtures/xxx_api.json
$ python manage.py runserver
```


### 事前準備3：Celeryプロセスの起動

```sh
# 別シェルで起動する
$ cd backend
$ pipenv shell
$ celery -A xxx_api worker -l info --pool=solo
```

<b>これでCeleryプロセスの実行準備が完了しました。</b>


### （必要に応じて）：flower(Celeryタスクの管理ツール)の起動

* これを実行すると、Web画面からCeleryタスク状況が確認できるようになります。
* http://localhost:5555

```sh
# 別シェルで起動する
$ cd backend
$ pipenv shell
$ celery flower -A xxx_api --address=127.0.0.1 --port=5555
```

### （必要に応じて）：Angularの実行

```sh
$ cd frontend/poc-frontend
$ npm install
$ ng serve
```


### （必要に応じて）：AngularフロントエンドからCeleryプロセスを実行する場合

![screen](http://www.rinsymbol.sakura.ne.jp/github_images/angular_job_management.png)

* 以下のURLにアクセス
  * http://localhost:4200/
  * 処理対象ファイルを選択(program_language.xlsx)
  * 処理実行ボタンをクリック
  * Celeryプロセスのコンソールに以下のようなメッセージが表示されればOK

```
[2021-03-22 00:17:12,563: WARNING/MainProcess] current_task_idです：3839db79-0d03-4096-9d88-7b30411ea681
[2021-03-22 00:17:13,953: INFO/MainProcess] Task xxx_api.tasks.do_parse_resource[3839db79-0d03-4096-9d88-7b30411ea681] succeeded in 1.3910000000
032596s: 'program_language.xlsxをParseResultに格納しました'
```


### Djangoバックエンド（Django REST frameworkのAPI）からCeleryプロセスを実行する場合

#### [1] 単純なCeleryプロセスを実行したい場合

* 以下のURLにアクセスし、Celeryプロセス実行
  * http://localhost:8000/xxx_api/v1
* 以下のURLから結果確認
  * http://localhost:8000/admin/django_celery_results/taskresult/
* やっていること
  * Django RESTFrameworkのエンドポイント経由で```backend/xxx_api/tasks.py:do_something関数```を実行
  * Redisにメッセージキュー送信
  * RedisからCeleryに処理依頼
  * do_somethingの戻り値("start")がResult Dataとして登録

#### [2] Excelデータ(BinaryResource)をParseResultに書き込む場合

* 以下のURLにアクセスし、Celeryプロセス実行
  * http://localhost:8000/xxx_api/v1/do_parse_resource/

```json
// POSTパラメータ
{"resource_id": "cc42c989-6813-456f-87ab-16858ef38fd9"}
```

* DBテーブル(ParseResult)にデータが格納されていることを確認するため、以下にアクセス(Adminerを利用。)
  * http://localhost:8080/
* ログイン情報を入力
  * データベース種類：PostgreSQL
  * サーバ: db
  * ユーザ名: admin
  * パスワード: admin
  * データベース: poc
* テーブル一覧のうち、```xxx_api_parseresult```を参照し、データが格納されていることを確認



## コンテナごとの接続情報

* Redis(MQ)

|イメージ|ホスト名|ポート番号(ホスト)|ポート番号(コンテナ)|
|----------|--------|----------|------|
|redis:6.2.1|mq|6379|6379|

* PostgreSQL

|イメージ|ホスト名|DB名|ユーザ名|パスワード|ポート番号(ホスト)|ポート番号(コンテナ)|
|----------|--------|----|--------|----------|----------|----|
|postgres:13|db|poc|admin|admin|5432|5432|

* Adminer

|イメージ|ホスト名|ポート番号(ホスト)|ポート番号(コンテナ)|
|----------|--------|----------|----|
|adminer:latest|adminer|8080|8080|


## [備忘録] Celery4.xのWindowsでの動作について

Celery4.x以降はWindowsではサポートされないため、通常のコマンド```celery -A xxx_api worker -l info```では動かない。
<del>pipでeventletかgeventをインストールして以下のように実行する必要あり</del>

```sh
$ celery -A xxx_api worker -l info --pool=solo 
```



[参考資料]

* https://stackoverflow.com/questions/62524908/task-receive-but-doesnt-excute 
* https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows
* https://stackoverflow.com/questions/60179472/databasewrapper-objects-created-in-a-thread-can-only-be-used-in-that-same-thread 

## [備忘録] Djangoモデルから取得したバイナリ（Excelファイル）を読み込むには？

* 下記のもので対応可能
  * io.BytesIO
  * pandas
  * xlrd：2.x系はxlsサポートをしないため、pandasからopenpyxlを入れるように言われる
  * openpyxl



```python
import io
import pandas as pd

record = HogeModel.objects.get(pk="hoge")
df = pd.read_excel(io.BytesIO(record.blob_data))
```


## その他

### pipenv installしたくない人向け 

```sh
$ pip install django
$ pip install djangorestframework 
$ pip install celery 
$ pip install django-celery-results 
$ pip install psycopg2 
$ pip install redis 
$ pip install eventlet
$ pip install black
$ pip install flake8
$ pip install openpyxl
$ pip install xlrd
$ pip install flower
```
