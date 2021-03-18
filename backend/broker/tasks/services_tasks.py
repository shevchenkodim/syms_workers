from celery import app


@app.shared_task()
def test_shared_task():
    """ Test task """
    pass
