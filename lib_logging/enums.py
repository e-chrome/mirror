import logging
from enum import Enum


class LogLevelEnum(str, Enum):
    DEBUG = logging.getLevelName(logging.DEBUG)
    INFO = logging.getLevelName(logging.INFO)
    WARNING = logging.getLevelName(logging.WARN)
    ERROR = logging.getLevelName(logging.ERROR)
    FATAL = logging.getLevelName(logging.FATAL)


class EnvEnum(str, Enum):
    LOCAL = 'Local'
    STAGING = 'Staging'
    PRODUCTION = 'Production'
