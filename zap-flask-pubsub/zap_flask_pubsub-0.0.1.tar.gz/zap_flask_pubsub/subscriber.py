import json
from zap_flask_pubsub.factory import BrokerFactory


class Subscriber:
    def __init__(self, app):
        self.app = app
        self.broker = BrokerFactory.get_broker(app)

    def setup(self):
        queues = json.load(open(self.app.config.get('PUBSUB_SUBSCRIPTION_LIST')))
        self.broker.run(queues)
