
# Resources

Useful resources for use with this repository.


# docker-compose: Kafka &  Zookeeper

I've included a docker-compose file for zookeeper+kafka and you should be able to log directly to it with this wrapper.

However, be aware the docker image includes metrics for the supporting company.

To use:
* `docker-compose up` to start zookeeper and kafka
* `docker ps` to get the container id for kafka (confluent_kafka)
* `docker exec -it <container name> /bin/bash` to get onto that box.
* `kafka-console-consumer --bootstrap-server localhost:9092 --topic <kafka_topic>--from-beginning` for view all messages logged to your kafka topic.
