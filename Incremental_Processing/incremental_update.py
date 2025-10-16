#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Incremental Data Processor
Consumes CDC events from 'cdc_topic' and updates a simple in-memory model
Linux/Ubuntu Compatible
"""

from kafka import KafkaConsumer
import json
from collections import defaultdict

# In-memory "database" to track values
database = defaultdict(float)

consumer = KafkaConsumer(
    'cdc_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='cdc_group'
)

print("📡 Incremental Processor started. Listening to 'cdc_topic'...")

try:
    for msg in consumer:
        event = msg.value
        op = event['operation']
        rid = event['record_id']
        val = event.get('value', 0)

        if op == 'insert':
            database[rid] = val
        elif op == 'update':
            database[rid] = val
        elif op == 'delete':
            if rid in database:
                del database[rid]

        print(f"✅ Event: {event} | Updated database: {dict(database)}")

except KeyboardInterrupt:
    print("\n🛑 Stopping Incremental Processor...")
finally:
    consumer.close()
