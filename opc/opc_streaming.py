from confluent_kafka import Consumer, KafkaException, KafkaError
from pymongo import MongoClient
import json
import psycopg2

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

# Set up PostgreSQL connection
conn = psycopg2.connect(
    host='db',
    port='5432',
    dbname='postgres',
    user='username',
    password='password'
)
# conn = psycopg2.connect("postgresql://admin:admin@local_pgdb:5432/opc_server")
conn.autocommit = True
cursor = conn.cursor()

#check table if exist
# def table_exists(table_name):
#     cursor.execute("""
#         SELECT EXISTS (
#             SELECT 1
#             FROM information_schema.tables
#             WHERE table_name = %s
#         )
#     """, (table_name,))
#     return cursor.fetchone()[0]


table_name = 'opc_sensors'

# if not table_exists(table_name):
#     cursor.execute(f"""
#         CREATE TABLE {table_name} (
#             timestamp datatype1,
#             column2 datatype2,
#             -- Add more columns as needed
#         )
#     """)
# Prepare SQL statement
sql_insert = "INSERT INTO opc_sensors (datatime, opc_pressure,opc_temperature) VALUES (%s, %s, %s)"

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
        # Insert data into PostgreSQL
        # print(value['timestamp'])
        cursor.execute(sql_insert, (value['timestamp'], value['opc_pressure'], value['opc_temperature']))
        # Manually commit the offset to mark the message as processed
        consumer.commit(msg)

    except KeyboardInterrupt:
        break

consumer.close()  # Close the Kafka consumer and PostgreSQL connection
# cursor.close()
# conn.close()
