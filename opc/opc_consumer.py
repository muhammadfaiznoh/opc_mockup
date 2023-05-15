# import asyncio
# from asyncua import Client, ua

# async def main():
#     # url = "opc.tcp://172.16.247.85:4840/G01"
#     # namespace = "weintek"   
#     url = "opc.tcp://host.docker.internal:4840/freeopcua/server/"
#     namespace = "http://examples.freeopcua.github.io"
#     print(f"Connecting to {url} ...")
#     async with Client(url=url) as client:
        
#         X = {}
#         # sensors = ['X1','X2', 'X3','X7', 'X8']
#         # for x in sensors:
#         node = client.get_node("ns=2;i=2")
#         name = (await node.read_browse_name()).Name
#         value = (await node.read_value())
#         return value
    

# print(asyncio.run(main()))


from kafka import KafkaConsumer
import json

# Create Kafka consumer instance
consumer = KafkaConsumer(
    'opc_server'
)

# Consume and print messages from Kafka
for message in consumer.poll(timeout_ms=1000):
    print(message.value)

# Close the consumer
consumer.close()