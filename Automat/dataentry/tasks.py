from automat_main.celery import app
import time


@app.task
def celery_test_task():
    time.sleep(10)
    return "Task executed successfully."