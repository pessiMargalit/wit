import logging


class Logger:
    _level = logging.DEBUG
    _format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
    logging.basicConfig(format=_format, level=_level)
    _logger = logging.getLogger(__name__)

    @classmethod
    @property
    def logger(cls):
        return cls._logger

    # @classmethod
    # @logger.setter
    # def logger(cls, level=logging.INFO, format="MSG: %(message)s", file_handler=None):
    #     cls._level = level
    #     cls._format = format
    #     if file_handler:
    #         # cls._fileHandler = file_handler
    #         # file_handler = "wit_logger.txt"
    #         logging.basicConfig(format=format, level=level, fileHandler=file_handler)
    #     else:
    #         logging.basicConfig(format=format, level=level)
