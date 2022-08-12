import logging
import pickle
from datetime import timedelta
from typing import Optional, List

from django.db import models
from django.utils import timezone

from simpleworker.simple_task import SimpleTask

logger = logging.getLogger(__name__)


def serialize_class(cls):
    obj_dict = cls.__dict__
    text_representations = []
    for key, value in obj_dict.items():
        text_representations.append(key + " : " + str(value))

    return '\n'.join(text_representations)


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.TextField()
    args = models.TextField()
    payload = models.BinaryField()
    tries = models.IntegerField(default=0)
    next_try = models.DateTimeField(default=timezone.now)
    last_error = models.TextField(null=True, blank=True)
    queue = models.TextField(default='default')
    priority = models.IntegerField(default=0)

    @staticmethod
    def add(task: SimpleTask, next_try_seconds: Optional[int] = None):
        db_task = Task()
        db_task.name = task.__class__.__name__
        db_task.args = serialize_class(task)
        db_task.payload = pickle.dumps(task)
        db_task.queue = task.queue
        db_task.priority = task.priority
        if next_try_seconds is not None:
            db_task.next_try = timezone.now() + timedelta(seconds=next_try_seconds)

        db_task.save()
        logger.info(f'Added task {task.__class__.__name__} with id {db_task.id}. Scheduled to run at {db_task.next_try}')
        return db_task

    @staticmethod
    def get_next(db='default', queues: Optional[List] = None):
        tasks = Task.objects.using(db).select_for_update(skip_locked=True).filter(next_try__lte=timezone.now())
        if queues is not None:
            tasks = tasks.filter(queue__in=queues)
        task = tasks.order_by('-priority', 'id').first()
        return task

    def __str__(self):
        return f'{self.name} {self.args}'


class TaskResult(models.Model):
    name = models.TextField()
    args = models.TextField()
    payload = models.BinaryField()
    queue = models.TextField()
    result = models.BinaryField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    started = models.DateTimeField()
    finished = models.DateTimeField(default=timezone.now)

    @staticmethod
    def add(origin_task: Task, result=None, error: Optional[str] = None):
        TaskResult.objects.update_or_create(
            id=origin_task.id,
            defaults={
                'id': origin_task.id,
                'started': origin_task.created_at,
                'payload': origin_task.payload,
                'result': result,
                'error': error,
                'queue': origin_task.queue,
                'name': origin_task.name,
                'args': origin_task.args,
            }
        )
        logger.info(f"Task with id {origin_task.id} finished")
