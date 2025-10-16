#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spark Kafka Consumer - Real-Time Streaming
Linux/Ubuntu Compatible
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, from_json
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

# ------------------------------
# Initialize Spark Session
# ------------------------------
spark = SparkSession.builder \
    .appName("SparkKafkaConsumer") \
    .getOrCreate()

print("📡 Spark Kafka Consumer Started. Listening to 'sensor_data' topic...")

# ------------------------------
# Define schema for incoming JSON messages
# ------------------------------
schema = StructType([
    StructField("sensor_id", IntegerType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True)
])

# ------------------------------
# Read streaming data from Kafka
# ------------------------------
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert value column from JSON string to DataFrame columns
values = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# ------------------------------
# Compute rolling averages by sensor_id
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

query.awaitTermination()
