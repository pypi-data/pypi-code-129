import json
import pika

from zap_flask_pubsub.brokers.broker import Broker, validate_queues


class RabbitMQBroker(Broker):
    @classmethod
    def get_connection(cls, app):
        credentials = pika.PlainCredentials(app.config.get('RABBITMQ_USER'),
                                            app.config.get('RABBITMQ_PWD'))
        return pika.BlockingConnection(pika.ConnectionParameters(
            'localhost',
            app.config.get('RABBITMQ_PORT'), '/',
            credentials))

    def publish(self, data, routing_key, exchange=''):
        connection = RabbitMQBroker.get_connection(self.app)
        channel = connection.channel()

        channel.queue_declare(queue=routing_key)
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=json.dumps(data))
        connection.close()

    def run(self, queues):
        '''
        :param queues:[{id:<queue_id>}, callback:<callback_function>]
        :return: None
        '''
        validate_queues(queues)
        connection = RabbitMQBroker.get_connection(self.app)
        channel = connection.channel()
        for queue in queues:
            channel.queue_declare(queue=queue.get('routing_key'))
            #  channel.basic_consume(queue=queue.get('id'), on_message_callback=queue.get('callback'))
            callback = getattr(self.callback_functions, queue.get('callback'))
            channel.basic_consume(queue=queue.get('routing_key'), on_message_callback=callback)
        print('Subscriber is listening...')
        channel.start_consuming()
