How to Run in Ubuntu/Linux

Place dataset.csv in the InMemory_Processing folder

cd ~/Documents/DataProcessingProject/InMemory_Processing
ls
# Should show: spark_inmemory.py  dataset.csv


Make script executable

chmod +x spark_inmemory.py


Run the script

./spark_inmemory.py


or

python3 spark_inmemory.py


Expected output

📡 Spark In-Memory Processing Started
✅ Original DataFrame:
+----------+-----+-----+
|sensor_id |value|humid|
+----------+-----+-----+
|1         |10   |60   |
|2         |15   |58   |
|3         |20   |59   |
+----------+-----+-----+
💾 DataFrame cached in memory
✅ Aggregated Averages (In-Memory):
+-------+-------+
|avg_value|avg_humid|
+-------+-------+
|15.0    |59.0   |
+-------+-------+
🛑 Spark Session stopped