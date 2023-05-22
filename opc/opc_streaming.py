from confluent_kafka import Consumer, KafkaException, KafkaError
from pymongo import MongoClient
import json

conf = {
    'bootstrap.servers': 'kafka:19092',  # Kafka broker address
    'group.id': 'console-consumer-92606',        # Consumer group ID
    'auto.offset.reset': 'earliest',        # Start consuming from the beginning of the topic
    'enable.auto.commit': False             # Disable auto commit
}

consumer = Consumer(conf)

consumer.subscribe(['opc_server'])  # topic name

# Set the MongoDB connection details
mongodb_uri = 'mongodb://root:example@mongo:27017'
db_name = 'opc_sensors'
collection_name = 'sensors'

# Create a MongoDB client and connect to the database
client = MongoClient(mongodb_uri)
db = client[db_name]
collection = db[collection_name]


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
        value = json.loads(msg.value().decode('utf-8'))  # Assuming the message value is a string
        # Process the received message
        print(f'Received message: {value}')

        # Insert the message value into MongoDB
        collection.insert_one(value)
        # Manually commit the offset to mark the message as processed
        consumer.commit(msg)

    except KeyboardInterrupt:
        break

consumer.close()  # Close the Kafka consumer
