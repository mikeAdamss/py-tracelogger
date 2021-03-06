"""Logging module"""

import logging
import logger_constants as lc

from kafka_handler import KafkaHandler

# Our main logging class
class NewLogger(object):

    def __init__(self, nameSpace=None, handler=None, handlerArgs=None, logLevel=None):

        # ------------------------------
        # Sanity check the provided args

        if nameSpace == None:
            raise ValueError("Logger must be initialsed with a namespace keyword argument.")

        if handler not in lc.LOGGERS:
            raise ValueError("Logger must be initialsed with a valid logger choice. Got '{}' must be one of:".format(handler) + ",".join(lc.LOGGERS))

        if logLevel not in lc.LOG_LEVELS and logLevel != None:
            raise ValueError("Logger must be initialsed with a valid log level. Got '{}' must be one of".format() + ",".join(lc.LOG_LEVELS))

        if logLevel == None:
            logLevel = lc.DEBUG

        # Convert string log level to the appropriate int
        logLevel = lc.LOG_LEVEL_LOOKUP[logLevel]

        # ----------------------------
        # Initialise the chosen logger

        if handler == lc.KAFKA:
            self.logger = getKafkaHandler(nameSpace, logLevel, handlerArgs)

    # The writeLog mehod is intended to be overwritten to allow logging to a specification.
    def writeLog(self, record):
        return record

    # # Create a debug level log
    def debug(self, record):
        record = self.writeLog(record)
        self.logger.debug(record)

    # Create a warning level log
    def warning(self, record):
        record = self.writeLog(record)
        self.logger.warning(record)

    # Create a error level log
    def error(self, record):
        record = self.writeLog(record)
        self.logger.error(record)

    # Create a ingo level log
    def info(self, record):
        record = self.writeLog(record)
        self.logger.error(record)

    def close(self):
        self.logger.handlers[0].close()



# -----------------------------------------------
# -----------------------------------------------
# Each supported handler follows in its own block

# Kafka
def getKafkaHandler(nameSpace, logLevel, handlerArgs):

    if "kafka_topic" not in handlerArgs.keys():
        raise ValueError("To use a kafka logger, you need to provide a provide a handlerArgs dict which incudes a value for kafka_topic.")

    if "kafka_hostlist" not in handlerArgs.keys():
        raise ValueError("To use a kafka logger, you need to provide a handlerArgs dict which incudes a value for kafka_address.")

    logger = logging.getLogger(nameSpace)
    logger.setLevel(logLevel)

    kh = KafkaHandler(topic=handlerArgs["kafka_topic"], hostlist=handlerArgs["kafka_hostlist"])
    logger.addHandler(kh)

    return logger
