import logging
from os import environ
from celery import Celery
from celery.utils.log import get_task_logger

print("start")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[logging.StreamHandler()])
                    
logger = get_task_logger(__name__)
logger.propagate = True

celery_app = Celery(
    broker=environ.get("BROKER"), # "sqs://"
    broker_url=environ.get("BROKER_URL"), # "sqs://foo:bar@localstack:4566",
    backend=environ.get("RESULT_BACKEND"),
)

@celery_app.task()
def add(a,b):
    logger.warning(f'add {a} {b}')
    print(f'add {a} {b}')
    logging.warning(f'add {a} {b}')
    
def init_celery():
    
    celery_app.conf.update(
        broker_transport_options={
            "region": "eu-central-1",
            "visibility_timeout": 30,
            "wait_time_seconds": 30,
            "predefined_queues": {"celery": {"url": environ.get("QUEUE_URL")}}, # http://localstack:4566/000000000000/queue1
        },
    )
    
    print('ready')
    
if __name__ == "__main__":
    init_celery()
    
# start worker
# celery --app app worker --loglevel INFO | DEBUG
