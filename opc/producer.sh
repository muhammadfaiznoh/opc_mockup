#!/bin/bash

kafka-console-producer \
  --broker-list localhost:9092 \
  --topic opc_server
