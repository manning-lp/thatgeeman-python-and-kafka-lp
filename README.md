# python-and-kafka-lp-author
Repository for liveProject: Python and Kafka

To run the code, use: 

```bash

poetry run python src/main.py

```

# docker compose, kafka and zookeper

The containers are connected via a network `python-kafka-net`. To build the containers use `docker compose up -d`. 

To verify if the networks are established within the containers and the localhost, run 
for each exposed port: `echo "srvr" | nc localhost 2181 ; echo` (zookeeper) and `echo "srvr" | nc localhost 9092 ; echo` for kafka.

Testing the containers: In two containers for the consumer side, do:
`docker compose exec -it kafka  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --list`

For the producer side: 
`docker compose exec -it kafka  /opt/bitnami/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --list`
