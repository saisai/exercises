from celery import Celery

APP_NAME = 'tasks'
BROKER_NAME = 'redis://localhost:6379/0'
#BROKER_NAME = '"amqp://guest:guest@localhost:5672//"'
BACKEND = 'db+postgresql://scrapyuser:scrapypassword@localhost/scrapy'
#BACKEND = 'db+postgresql://postgres:postgres@localhost/celerydemo'

app = Celery(APP_NAME,broker=BROKER_NAME, backend=BACKEND)

@app.task
def reverse(string):
    return string[::-1]
