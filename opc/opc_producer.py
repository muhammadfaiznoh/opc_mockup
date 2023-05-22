#import libraries

import asyncio
import time
import json
from asyncua import Client
from kafka import KafkaProducer



def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    
    
producer = KafkaProducer(bootstrap_servers='kafka:19092')

async def main():
    url = "opc.tcp://host.docker.internal:4840/freeopcua/server/" 
    sensorNode = ["ns=2;s=freeopcua.Tags.pressure", "ns=2;s=freeopcua.Tags.temperature"]

    async with Client(url=url) as client:
        while True:
            value = []
            for sensor in sensorNode:
                node = client.get_node(sensor)
                value.append(await node.read_value())
            message = {
            "timestamp": time.time(),
            "opc_pressure": value[0],
            "opc_temperature": value[1]
            }
            json_data = json.dumps(message)
            
            #send opc data in json format to kafka producer
            producer.send('opc_server', json_data.encode()).add_callback(on_send_success).add_errback(on_send_error)
            print(message)
            producer.flush()
            time.sleep(1)

if __name__ == "__main__":
    
    # Read OPC data
    asyncio.run(main())


