from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

app = Celery('test_project')

# создаем очередь и привязываем ее к бирже BaseExchange
app.conf.task_queues =(
    Queue('test_app_queue',
          Exchange('BaseExchange', type='topic'),
          routing_key='test_app.*', max_priority=10),
          # routing_key - ключ маршрутизации, определяющий в какую очередь отправить сообщение
          # max_priority - указание максимального приоритета задач в очереди
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
