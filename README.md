# 各タスクの設定

# CloudRun Service

## 開発環境設定

### コンテナイメージ ビルドと起動

```bash
$ cd service/
$ docker compose up --build
```

### Firebaseエミュレータの確認
以下へアクセスできるか確認
http://127.0.0.1:4000/


### Curlによる疎通確認
```bash
# dataはbase64エンコードした値
$ curl -X POST http://localhost:8080/ \
    -H "Content-Type: application/json" \
    -d '{"message": {"data": "SGVsbG8gd29ybGQ="}}'
```


## Google Cloudへデプロイ
### コンテナイメージビルドとpush

```bash
$ cd service/docker/run/
```

```bash
$ gcloud builds submit --tag asia-northeast1-docker.pkg.dev/{GoogleCloudプロジェクト名}/{ArtifactRegistry名}/{イメージ名}:{タグ名}
```

### CloudRun作成

```bash
gcloud run deploy {Run名} --image asia-northeast1-docker.pkg.dev/{GoogleCloudプロジェクト名}/{ArtifactRegistry名}/{イメージ名}:{タグ名} \  --no-allow-unauthenticated
```

### PubSubの疎通確認
```bash
gcloud pubsub topics publish {トピック名} --message "{任意の文字列}"
```

# CloudRun Jobs

## Google Cloudへデプロイ
```bash
$ cd jobs/
```

### コンテナイメージビルドとpush
```bash
$ gcloud builds submit --tag asia-northeast1-docker.pkg.dev/{GoogleCloudプロジェクト名}/{ArtifactRegistry名}/{イメージ名}:{タグ名}
```

### Jobs作成

```bash
$ gcloud run jobs create {ジョブ名}} \
    --image asia-northeast1-docker.pkg.dev/{GoogleCloudプロジェクト名}/{ArtifactRegistry名}/{イメージ名}:{タグ名} \
    --region asia-northeast1 \
    --set-env-vars SEND_ADDRESS={送信先メアド},ACCOUNT={送信元メアド},PASSWORD={アプリケーションパスワード}
```

### Jobs実行

```bash
$ gcloud run jobs execute {ジョブ名}
```

## 参考
- [Cloud Run で Python ジョブをビルドして作成する](https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python?hl=ja)
- [Pythonを使って、Gmailを送信する方法](https://note.com/noa813/n/nde0116fcb03f)
