#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CDC Producer - Simulates database changes
Sends change events to Kafka topic 'cdc_topic'
Linux/Ubuntu Compatible
"""

from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Starting CDC Producer... Sending database change events to 'cdc_topic'")

try:
    while True:
        # Simulate insert/update/delete
        operation = random.choice(['insert', 'update', 'delete'])
        record = {
            'operation': operation,
            'record_id': random.randint(1, 10),
            'value': round(random.uniform(10, 100), 2)
        }
        producer.send('cdc_topic', value=record)
        print(f"✅ Sent CDC event: {record}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Stopping CDC Producer...")
finally:
    producer.close()
