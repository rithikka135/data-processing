How to Run in Ubuntu/Linux

Make scripts executable

cd ~/Documents/DataProcessingProject/Incremental_Processing
chmod +x cdc_producer.py incremental_update.py


Ensure Kafka is running

sudo systemctl start zookeeper
sudo systemctl start kafka
kafka-topics.sh --create --topic cdc_topic --bootstrap-server localhost:9092


Run incremental processor (consumer) in one terminal:

./incremental_update.py


Run CDC producer in another terminal:

./cdc_producer.py


Expected output:

📡 Incremental Processor started. Listening to 'cdc_topic'...
✅ Event: {'operation': 'insert', 'record_id': 3, 'value': 45.67} | Updated database: {3: 45.67}
✅ Event: {'operation': 'update', 'record_id': 3, 'value': 55.12} | Updated database: {3: 55.12}
✅ Event: {'operation': 'delete', 'record_id': 3, 'value': 55.12} | Updated database: {}
