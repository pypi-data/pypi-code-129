from zap_flask_pubsub.brokers.rabbit_mq import RabbitMQBroker


class BrokerFactory:
    @staticmethod
    def get_broker(app):
        if app.config.get('RABBITMQ_USER') and app.config.get('RABBITMQ_PWD'):
            return RabbitMQBroker(app)
        else:
            raise Exception('Broker is not configured')
