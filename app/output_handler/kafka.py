from confluent_kafka import Producer

from output_handler import OutputHandler


class Kafka(OutputHandler):
    def __init__(self, metadata, data, bootstrap_servers=None, topic=None) -> None:
        
        metadata['bootstrap_servers'] = bootstrap_servers
        metadata['topic'] = topic

        self.sink(metadata, data)

    def sink(self, metadata, data):
        bootstrap_servers = metadata.get('bootstrap_servers')
        topic = metadata.get('topic')

        if not (bootstrap_servers or topic):
            raise Exception(f'Kafka server details not provided. Could not connect.')
        
        producer = Producer({'bootstrap.servers': bootstrap_servers})

        for message in data:
            message = ','.join(map(str, message))
            producer.produce(topic, value=message)


        producer.flush()

