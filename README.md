# 各タスクの設定

## CloudRun Service
wip...

## CloudRun Jobs

### コンテナイメージビルドとpush
```bash
$ gcloud builds submit --tag asia-northeast1-docker.pkg.dev/{GoogleCloudプロジェクト名}/{ArtifactRegistry名}/{イメージ名}:{タグ名}
```

### Jobs作成

```bash
$ cd pubsub_jobs/
```

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