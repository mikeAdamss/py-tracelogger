
import logging


# Log Levels
DEBUG = "debug"
WARNING = "warning"
ERROR = "error"
INFO = "info"
LOG_LEVELS = [DEBUG, WARNING, ERROR, INFO]


# Lookup log levels as integers
LOG_LEVEL_LOOKUP = {
        "debug":logging.DEBUG,
        "warning":logging.WARNING,
        "info":logging.INFO,
        "error":logging.ERROR
}

# ------------------
# Supported handlers

KAFKA = "Kafka"
LOGGERS = [KAFKA]
