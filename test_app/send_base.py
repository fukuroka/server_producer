from typing import Optional

from test_project.celery import app

class SendBase:
    """Базовый класс для отправки сообщений на другой микросервис"""
    def __init__(self, task_name, args=None, kwargs=None, priority=0, exchange='BaseExchange', routing_key='') -> None:
        self.task_name = task_name # путь до селери задачи на втором микросервисе вида
        # "<название джанго приложения>.<путь до файла с тасками>.<название таски>"
        # например в этом проекте TestRC.task.add_name
        # файлы отправляются в байтах
        self.args = args or []
        self.kwargs = kwargs or {}
        self.priority = priority # приоритет задачи от 0 до 9, где 9 максимальный приоритет
        self.exchange = exchange # указание биржи
        self.routing_key = routing_key # ключ маршрутизации, определяющий в какую очередь отправить задачу

    def get_result(self,timeout=40) -> Optional:
        """Отправляет задачу на микросервис через Celery"""
        task = app.send_task(
            self.task_name,
            args=self.args,
            kwargs=self.kwargs,
            priority=self.priority,
            exchange=self.exchange,
            routing_key=self._generate_routing_key(),
        )
        return task.get(timeout=timeout) # время, в течение которого будем ожидать ответ

    def _generate_routing_key(self) -> str:
        """Формирование ключа маршрутизации"""
        parts = self.task_name.split('.')
        return f'{parts[0]}.{parts[2]}'