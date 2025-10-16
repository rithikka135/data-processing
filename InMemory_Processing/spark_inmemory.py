#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In-Memory Data Processing using Spark
Linux/Ubuntu Compatible
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# ------------------------------
# Initialize Spark Session
# ------------------------------
spark = SparkSession.builder \
    .appName("InMemoryProcessing") \
    .getOrCreate()

print("📡 Spark In-Memory Processing Started")

# ------------------------------
# Load dataset (CSV) into Spark DataFrame
# ------------------------------
input_path = "dataset.csv"  # Make sure dataset.csv is in the same folder
try:
    df = spark.read.csv(input_path, header=True, inferSchema=True)
except Exception as e:
    print(f"❌ Error reading {input_path}: {e}")
    exit(1)

print("✅ Original DataFrame:")
df.show()

# ------------------------------
# Cache the DataFrame in memory
# ------------------------------
df.cache()
print("💾 DataFrame cached in memory")

# ------------------------------
# Perform simple aggregation: average of numeric columns
# ------------------------------
numeric_cols = [c for c, t in df.dtypes if t in ('int', 'double', 'float')]
if numeric_cols:
    agg_exprs = [avg(col(c)).alias(f"avg_{c}") for c in numeric_cols]
    agg_df = df.agg(*agg_exprs)
    print("✅ Aggregated Averages (In-Memory):")
    agg_df.show()
else:
    print("⚠️ No numeric columns found for aggregation")

# ------------------------------
# Stop Spark Session
# ------------------------------
spark.stop()
print("🛑 Spark Session stopped")
