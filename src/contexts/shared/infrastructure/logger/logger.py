import logging
import logging.config

from contexts.shared.infrastructure.logger.config import LOGGING_CONFIG


class Logger:
    def __init__(self, name: str) -> None:
        self._default_level = logging.INFO
        self._logger = logging.getLogger(name.capitalize())

        self._setup()

    def _setup(self) -> None:
        logging.config.dictConfig(LOGGING_CONFIG)

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def critical(self, message: str) -> None:
        self._logger.critical(message)
