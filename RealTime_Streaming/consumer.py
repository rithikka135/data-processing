#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kafka Consumer + Spark Streaming Processor
Linux/Ubuntu Compatible
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, from_json
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

# ------------------------------
# Initialize Spark Session
# ------------------------------
spark = SparkSession.builder \
    .appName("KafkaStreamProcessor") \
    .getOrCreate()

# ------------------------------
# Define schema for Kafka JSON messages
# ------------------------------
schema = StructType([
    StructField("sensor_id", IntegerType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True)
])

# ------------------------------
# Read data stream from Kafka
# ------------------------------
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert Kafka message value from JSON string to DataFrame columns
values = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# ------------------------------
# Compute rolling averages
# ------------------------------
agg = values.groupBy("sensor_id").agg(
    avg("temperature").alias("avg_temp"),
    avg("humidity").alias("avg_humid")
)

# ------------------------------
# Output results to console
# ------------------------------
query = agg.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

print("📡 Spark Streaming Processor started. Listening to 'sensor_data' topic...")

query.awaitTermination()
