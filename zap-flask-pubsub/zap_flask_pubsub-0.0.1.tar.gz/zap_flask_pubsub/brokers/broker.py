import importlib
import threading
from abc import ABCMeta, abstractmethod


class Broker():
    __metaclass__ = ABCMeta

    def __init__(self, app):
        self.app = app
        try:
            self.callback_functions = importlib.import_module(app.config.get('PUBSUB_SUBSCRIPTION_CALLBACK'))
        except Exception as e:
            raise Exception('Please define PUBSUB_SUBSCRIPTION_CALLBACK in settings file')

    @classmethod
    @abstractmethod
    def get_connection(cls):
        """Return Broker connections"""

    @abstractmethod
    def run(self, queues):
        """Consuming message stream"""

    @abstractmethod
    def publish(self, data, routing_key, exchange=''):
        """publish the data in message queue"""


def validate_queues(queues):
    if type(queues) != list:
        raise Exception('queues must be a list')
