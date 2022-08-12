from distutils.util import strtobool
from typing import Optional

from django.conf import settings


class SimpleTask:
    queue: str = 'default'
    max_retries: Optional[int] = None
    cron: Optional[str] = None
    # Tasks with higher priority are executed first
    priority: int = 100

    def _send(self, seconds_delay: Optional[int] = None):
        if hasattr(settings, 'SIMPLE_WORKER_SYNC_PROCESSING') and strtobool(str(settings.SIMPLE_WORKER_SYNC_PROCESSING)):
            self.handle()
        else:
            from simpleworker.models import Task
            Task.add(self, seconds_delay)

    def send(self):
        self._send()

    def send_delayed(self, seconds_delay: int):
        self._send(seconds_delay)

    def handle(self):
        raise NotImplementedError('Handle method must be implemented')
