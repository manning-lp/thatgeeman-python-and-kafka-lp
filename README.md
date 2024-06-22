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

# postgres db setup

Download sample dataset [pagilla](https://github.com/devrimgunduz/pagila). The dataset conntents are here: https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

You can load them via psql, pgAdmin, etc.
To do that we need the libraries installed:
```sh
brew install libpq # for psql cli
brew install postgresql@14 # for postgres14
```
To setup the user needed for postgres, follow the instructions here: https://gist.github.com/dnovais/c6c6894b95d764be2aca9736436edd0e

Download [DBeaver](https://dbeaver.io/). 

In the DBeaver, load the unzipped sql files and setup a conneciton to the database from the toolbar. Then set the schema.sql file as the schema from the toolbar.
Run schema.sql first. Now click on execute script for the data.sql file. If you get the COPY error, then that means we have to use the `psql` command to load the dataset.
DBeaver also lets you set user permissions, password etc. 

Thats done as follows:

```sh
/usr/local/Cellar/postgresql@14/14.12//bin/createuser -s postgres # add user 
psql -f ../Desktop/pagila-0.10.1/pagila-schema.sql -U postgres # use schema file as schema
psql -f ../Desktop/pagila-0.10.1/pagila-data.sql -U postgres # use the data file as databse, gets laoded to a database with the name "postgres"
```
now we can go in the cli command line to do `psql -U postgres` and run `\d` to show the tables under this user.

And run sql commands like `select actor_id, first_name from actor;`. Other SQL commands are here: https://www.w3schools.com/sql/sql_update.asp
To see if changes made to databse was saved, explore the table with the DBeaver tool and refresh.

Following should work to setup docker compose: https://github.com/devrimgunduz/pagila?tab=readme-ov-file#create-database-on-docker

In the docker-compose, although no password, we have to explicitly set the environment variable POSTGRES_PASSWORD=""  

`psycopg[binary]` is the name of the library that can execute SQL commands via python interface. Basic usage is here: https://www.psycopg.org/psycopg3/docs/basic/usage.html


# faust

1. Install faust-streaming (community edition of faust)
2. Run `docker compose up -d`
3. To consume messages from a topic called `greetings` (full history):
   1. `docker compose exec -it kafka  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic greetings --from-beginning`
   2. This executes the consumer 
   3. Alternatively, On a different terminal run `python src/faust_app.py worker -l info` to run the consumer
      1. This terminal will show the consumer logs, but only since program start (limited history).
4. Now send messages from the `faust_app.py` script and showing up in the consumer window!
   1. Execute `faust -A faust_app send @greet "Hello Faust"` based on the [guide](https://faust-streaming.github.io/faust/playbooks/quickstart.html)
   2. This part is the creator. 