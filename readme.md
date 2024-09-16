# Streaming data sink pipline with msk and emr

## Archtecture  (with flink/spark streaming)

IOT/Streaming data source -> kafka -> flink/spark steaming -> s3


## Steps:

### Find dataset
```
https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/iot_23_datasets_small.tar.gz
```

### Download it to EC2 and decompress it.

```
wget https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/iot_23_datasets_small.tar.gz

tar -zxvf iot_23_datasets_small.tar.gz
```

### Create msk cluster:
```
arn:aws:kafka:eu-west-1:855103261293:cluster/kakfka-flink/3184014b-1645-4bc5-8f73-c445e9826f30-6
```
### Create kafka topic with kafka client in EC2
```
wget https://archive.apache.org/dist/kafka/3.5.1/kafka_2.13-3.5.1.tgz

tar -xzf kafka_2.13-3.5.1.tgz

cd kafka_2.13-3.5.1/bin

./kafka-topics.sh --create --bootstrap-server b-1.kakfkaflink.w3luga.c6.kafka.eu-west-1.amazonaws.com:9092 --replication-factor 3 --partitions 1 --topic MSKTestTopic

>> Created topic MSKTestTopic.
```
### Create emr cluster: 

I use the emr here . (j-3DJHT6NC2IX61)

### Make msk & emr connected

Setting the security group of msk and emr cluster.

### Install jar & chmod

```
wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.2.0-1.18/flink-sql-connector-kafka-3.2.0-1.18.jar

wget https://repo.maven.apache.org/maven2/org/apache/kafka/kafka-clients/3.5.1/kafka-clients-3.5.1.jar

chmod 700 flink-connector-kafka-3.0.1-1.18.jar

chmod 700 kafka-clients-3.5.1.jar
```

### Run flink job (remember setting your s3 bucket on code kafka_to_s3.py)

```
flink run -m yarn-cluster -py kafka_to_s3.py --jarfile flink-sql-connector-kafka-3.2.0-1.18.jar --jarfile kafka-clients-3.5.0.jar
```

### Run steaming_data_producer.py on ec2

```
python3 streaming_data_producer.py 
```

### Check the sink data on s3 path
