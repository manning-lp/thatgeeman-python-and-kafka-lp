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

# postgres db 

Download sample dataset [pagilla](https://github.com/devrimgunduz/pagila). You can load them via psql, pgAdmin, etc.
```sh
brew install libpq # for psql cli
brew install postgresql@14 # for postgres14
```
To setup the user needed for postgres, follow the instructions here: https://gist.github.com/dnovais/c6c6894b95d764be2aca9736436edd0e

Download [DBeaver](https://dbeaver.io/). 

In the DBeaver, load the unzipped sql files and setup a conneciton to the database from the toolbar. Then set the schema from the schema.sql file.
Now click on execute script. Similary open the pagilla-data.sql file and execute. Skip errors.

^ this had to work, but for me what worked is:

```sh
/usr/local/Cellar/postgresql@14/14.12//bin/createuser -s postgres
psql -f ../Desktop/pagila-0.10.1/pagila-data.sql -U postgres
psql -f ../Desktop/pagila-0.10.1/pagila-schema.sql -U postgres
```
now we can go in the cli command line to do `psql -U postgres` and run `\d` to show the tables in this user.

And run sql commands like `select actor_id, first_name from actor;`

Following should work from docker: https://github.com/devrimgunduz/pagila?tab=readme-ov-file#create-database-on-docker