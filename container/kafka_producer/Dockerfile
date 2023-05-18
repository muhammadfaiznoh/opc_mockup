# FROM python:3.7-slim

# RUN pip install \
#     asyncua==1.0.2 \
#     kafka-python \
#     watchdog

# WORKDIR /opt/opc_mockup/kafka

# COPY ../../kafka /opt/opc_mockup/kafka

# CMD [ "python" "./kafka_producer.py"]

FROM confluentinc/cp-kafka:5.3.1

ENV KAFKA_BROKER_ID 1
ENV KAFKA_ZOOKEEPER_CONNECT localhost:2181
ENV KAFKA_TOPIC opc_server

# WORKDIR /usr/bin/
WORKDIR /opt/opc_mockup/opc
# CMD ["kafka-console-producer", "--broker-list", "localhost:9092", "--topic", "opc_server"]
# CMD [ "ls" ]

COPY ../../opc /opt/opc_mockup/opc

RUN chmod +x /opt/opc_mockup/opc/producer.sh
# Set the execution permission for the script
# RUN chmod +x /producer.sh
# CMD [ "ls" ]
# Start the Kafka producer
CMD ["sh", "-c", "/opt/opc_mockup/opc/producer.sh && sleep infinity"]
