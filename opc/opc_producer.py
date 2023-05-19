# import time
# import OpenOPC
# from kafka import KafkaProducer
# import json

# # Connect to OPC server
# opc = OpenOPC.client()
# opc.connect('opc.tcp://0.0.0.0:4840/freeopcua/server/')

# # Connect to Kafka cluster
# producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9092'])

# # Define OPC tags to read
# tags = ['2']#['Channel1.Device1.Tag1', 'Channel1.Device1.Tag2', 'Channel2.Device2.Tag1']

# # Continuously read OPC data and send to Kafka
# while True:
#     # Read OPC data
#     data = opc.read(tags)

#     # Convert OPC data to JSON format
#     json_data = json.dumps(data)

#     # Send JSON data to Kafka
#     producer.send('my-first-topic', json_data.encode())

#     # Flush Kafka producer buffer
#     producer.flush()

#     # Sleep for some time before reading again
#     time.sleep(1)

import asyncio
import time
import json
import ping3
from asyncua import Client, ua
from kafka import KafkaProducer
from kafka.errors import KafkaError


def ping(host):
    response_time = ping3.ping(host)
    if response_time is not None:
        print(f"Host {host} is reachable. Response time: {response_time} ms")
    else:
        print(f"Host {host} is unreachable.")

# Example usage
ping("kafka")

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    
    
producer = KafkaProducer(bootstrap_servers='kafka:19092')
print(producer)
async def main():
    url = "opc.tcp://host.docker.internal:4840/freeopcua/server/"
    namespace = "weintek"   
    sensorNode = "ns=2;i=2"
    # url = "opc.tcp://host.docker.internal:4840/freeopcua/server/"
    # namespace = "http://examples.freeopcua.github.io"
    async with Client(url=url) as client:
        while True:
            node = client.get_node(sensorNode)
            name = (await node.read_browse_name()).Name
            value = (await node.read_value())
            message = {
            "timestamp": time.time(),
            "value1": value
            }
            json_data = json.dumps(message)
            
            producer.send('opc_server', json_data.encode()).add_callback(on_send_success).add_errback(on_send_error)
            print(message)
            producer.flush()
            time.sleep(1)
            # return value
    
    # while True:
    #     # Get the current values of the data points.
    #     value = (await node.read_value())

    #     # Generate a message.
    #     message = {
    #     "timestamp": time.time(),
    #     "value1": value
    #     }
    #     print(message)
    #     # Publish the message to the desired Kafka topic.
    #     producer.send('opc_server', json.dumps(message))

    #     # Sleep for a second.
    #     time.sleep(1)

    # handle exception
# data = asyncio.run(main(sensorNode))
# print(data)
if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    # asyncio.run(main(), debug=True)
    # while True:
    # Read OPC data
    asyncio.run(main())
    # print(data)

    # Convert OPC data to JSON format
    # json_data = json.dumps(data)

    # # Send JSON data to Kafka
    # producer.send('my-first-topic', json_data.encode())

    # # Flush Kafka producer buffer
    # producer.flush()

    # # Sleep for some time before reading again
    # time.sleep(1)

