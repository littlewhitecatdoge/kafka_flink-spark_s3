from kafka import KafkaProducer
import pandas as pd

### read data line one by one 
with open('~/data/opt/Malware-Project/BigDataset/IoTScenarios/CTU-Honeypot-Capture-4-1/bro/conn.log.labeled') as f:
    for line in f:
        print(line)
        line=str.encode(line)
        producer = KafkaProducer(bootstrap_servers='b-1.kakfkaflink.w3luga.c6.kafka.eu-west-1.amazonaws.com:9092')
        producer.send('MSKTestTopic', line)
        producer.flush()