from abc import ABCMeta

from zap_flask_pubsub.factory import BrokerFactory


class Publisher:
    __metaclass__ = ABCMeta

    def __init__(self, app):
        self.broker = BrokerFactory.get_broker(app)

    def publish(self, data, routing_key, exchange=''):
        self.broker.publish(data, routing_key, exchange)
