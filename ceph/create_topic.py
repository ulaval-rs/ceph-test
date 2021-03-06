import config
from client import sns


def create_http_topic(with_endpoint: bool = True):
    return sns.create_topic(
        Name=config.TOPIC_NAME,
        Attributes={
            'verify-ssl': 'false',
            # 'persistent': 'true'
        } | ({
            'push-endpoint': f'http://{config.MY_IP}:80'
        } if with_endpoint else {}),
    )


def create_amqp_topic(with_endpoint: bool = True, persistent: bool = False):
    return sns.create_topic(
        Name=config.TOPIC_NAME,
        Attributes={
            'amqp-exchange': config.RABBITMQ_EXCHANGE,
            'amqp-ack-level': 'broker',
            'persistent': 'true' if persistent else 'false'
        } | ({
            'push-endpoint': f'amqp://{config.MY_IP}:5672'
        } if with_endpoint else {}),
    )


if __name__ == '__main__':
    response = create_http_topic()

    # response = create_amqp_topic()
    print(response)
