from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092'  # Kafka broker address
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Failed to deliver message: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')


topic = 'opc_server'  # Replace 'my-topic' with the actual topic name

for i in range(10):
    # Create a message (value) to be produced
    message = f'Message {i + 1}'

    # Produce the message to the topic
    producer.produce(topic, value=message.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered
producer.flush()
