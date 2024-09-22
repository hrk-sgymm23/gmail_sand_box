# 各タスクの設定

## CloudRun Service
wip...

### コンテナイメージビルドとpush

```bash
$ cd service/
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

## CloudRun Jobs

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