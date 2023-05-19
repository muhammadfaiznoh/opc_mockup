from confluent_kafka import Consumer, KafkaException, KafkaError

conf = {
    'bootstrap.servers': 'kafka:19092',  # Kafka broker address
    'group.id': 'console-consumer-92606',        # Consumer group ID
    'auto.offset.reset': 'earliest',        # Start consuming from the beginning of the topic
    'enable.auto.commit': False             # Disable auto commit
}

consumer = Consumer(conf)

consumer.subscribe(['opc_server'])  # Replace 'my-topic' with the actual topic name

while True:
    try:
        msg = consumer.poll(1.0)  # Poll for new messages (1.0 second timeout)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Reached end of partition, continue to the next one
                continue
            else:
                raise KafkaException(msg.error())

        # Process the received message
        print(f'Received message: {msg.value().decode("utf-8")}')

        # Manually commit the offset to mark the message as processed
        consumer.commit(msg)

    except KeyboardInterrupt:
        break

consumer.close()  # Close the Kafka consumer
