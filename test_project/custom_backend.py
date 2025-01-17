from celery.backends.rpc import RPCBackend

class CustomRPCBackend(RPCBackend):

    def on_result_fulfilled(self, result):
        """Переопределение обработки завершения задачи и удаление очереди."""
        super().on_result_fulfilled(result)
        self.result_consumer.cancel_for(result.id) # удаление очереди обратного ответа

