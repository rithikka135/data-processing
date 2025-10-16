#!/bin/bash

# Kafka broker address
BROKER="localhost:9092"

# Create topics for project
kafka-topics.sh --create --topic sensor_data --bootstrap-server $BROKER --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic cdc_topic --bootstrap-server $BROKER --partitions 1 --replication-factor 1

echo "✅ Kafka topics created: sensor_data, cdc_topic"
