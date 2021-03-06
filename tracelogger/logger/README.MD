
# py-tracelogger : logger

My wrapper for logging.


## Kafka Logger

Simple kafka logger. Logs messages to chosen kafka topic.


### Create a standard logger

```python
from logger import NewLogger

# Create a logger
handlerArgs = {"kafka_hostlist":"localhost:9092", "kafka_topic":"kafka_logs_out"}
log = NewLogger(nameSpace="example-logger", logLevel="debug", handler="Kafka", handlerArgs=handlerArgs)

# Use it
log.debug({"message":""I am a message"}) # etc
```

results in logging
`"{'message': 'foo'}"`



### Create a custom logger

```python

# Create a custom log writer that adds a custom time stamp
class NewLoggerWithTime(NewLogger):
    def writeLog(self, record):
        record.update({"time":"<time goes here>"})
        return record

# Create our new logger
handlerArgs = {"kafka_hostlist":"localhost:9092", "kafka_topic":"lll-logs-out"}
log = NewLoggerWithTime(nameSpace="example-logger", logLevel="debug", handler="Kafka", handlerArgs=handlerArgs)

log.debug({"message":"I am a message"})

```

results in logging
`"{"message":""I am a message", "time":"<time goes here>"}"`


## Note

For dev purposes, there is a docker-compose file included in the ../resources directory.

I've included a docker-compose file for zookeeper+kafka and you should be able to log directly to it with this wrapper.

However, be aware the docker image includes metrics for the supporting company.

To use:
* `docker-compose up` to start zookeeper and kafka
* `docker ps` to get the container id for kafka (confluent_kafka)
* `docker exec -it <container name> /bin/bash` to get onto that box.
* `kafka-console-consumer --bootstrap-server localhost:9092 --topic <kafka_topic>--from-beginning` for view all messages logged to your kafka topic.




