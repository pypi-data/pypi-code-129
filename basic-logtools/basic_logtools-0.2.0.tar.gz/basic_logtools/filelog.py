import os
import logging
from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler
from datetime import timezone
from dataclasses import dataclass
from enum import IntEnum


class LogLevel(IntEnum):
    CRITICAL=50
    ERROR=40
    WARNING=30
    INFO=10
    NOTSET=0

    @classmethod
    def get(cls, name, default=0):
        NAME = name.upper()
        names = [n.name for  n in cls]
        if NAME in names:
            return cls[NAME].value
        return default


@dataclass
class LogFile:
    _logger_methods = (
        'debug', 
        'error', 
        'info', 
        'warning', 
        'critical',
        'exception')


    class_name: str
    hostname: str
    code: str
    path: str
    max_bytes: int = 3200240
    backup_count: int =  18
    base_level: str = 'INFO'


    def __post_init__(self):
        """
        params:

        clasname :: nombre de clase que lo ejecuta
        code :: codigo activo
        path :: ruta donde almacenará log
        """
        self.logpath = Path(self.path).resolve().absolute()
        self.logpath.mkdir(parents=True, exist_ok=True)
        # create log instance
        self.create_logger()


    def create_logger(self):
        logger = logging.getLogger(f"{self.class_name}_{self.code}")
        handler = RotatingFileHandler(
            self.file_path,
            mode='a',
            maxBytes=self.max_bytes,
            backupCount=self.backup_count)
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s  %(process)d %(pathname)s %(filename)s %(module)s %(funcName)s %(message)s')
        LOG_LEVEL = LogLevel.get(self.base_level, 0)
        handler.setLevel(LOG_LEVEL)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOG_LEVEL)
        self.__logger = logger
        self.__handler = handler

    @property
    def file_name(self):
        return f"{self.class_name}_{self.hostname}_{self.code}.log"

    @property
    def logger(self):
        return self.__logger

    @property
    def handler(self):
        return self.__handler

    def __getattr__(self, name):
        if name in LogFile._logger_methods:
            return getattr(self.__logger, name)
        return '-'

    def save(self, level, msg, *args, **kwargs):
        self.__logger.log(level, msg, *args, **kwargs)

    @property
    def file_path(self):
        return self.logpath / self.file_name

    def close(self):
        self.logger.removeHandler(self.__handler)
        self.handler.close()
        logging.shutdown()
