#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kafka Producer - Simulates IoT Sensor Data
Linux/Ubuntu Compatible
"""

from kafka import KafkaProducer
import json
import time
import random

# ------------------------------
# Initialize Kafka Producer
# ------------------------------
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Starting Kafka Producer. Sending data to 'sensor_data' topic...")

# ------------------------------
# Produce random sensor data
# ------------------------------
try:
    while True:
        data = {
            'sensor_id': random.randint(1, 5),
            'temperature': round(random.uniform(25, 35), 2),
            'humidity': round(random.uniform(40, 60), 2)
        }
        producer.send('sensor_data', value=data)
        print(f"✅ Sent: {data}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Stopping Kafka Producer...")
finally:
    producer.close()
