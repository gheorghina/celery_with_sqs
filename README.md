## Description

Setup celery with SQS

## Installation Guide

1) install

pip install -r requirements.txt

-or-

pip install celery[sqs]

2) start localstack

docker-compose up

3) start worker

```
celery --app app worker --loglevel INFO
```

4) start a task

```
// cmd
python
import app
app.work()
```