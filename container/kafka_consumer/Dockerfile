# FROM python:3.7-slim

# RUN pip install \
#     asyncua==1.0.2 \
#     kafka-python \
#     watchdog

# WORKDIR /opt/opc_mockup/kafka

# COPY ../../kafka /opt/opc_mockup/kafka

# CMD [ "python" "./kafka_consumer.py"]

FROM confluentinc/cp-kafka:latest

ENV KAFKA_BROKER_ID 1
ENV KAFKA_ZOOKEEPER_CONNECT localhost:2181
ENV KAFKA_TOPIC opc_server

CMD ["kafka-console-consumer", "--bootstrap-server", "localhost:29092", "--topic", "opc_server"]
