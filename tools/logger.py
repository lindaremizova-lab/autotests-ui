import sys

from loguru import logger


logger.remove()

logger.add(
    sys.stdout,
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {extra[name]} | {level} | {message}"
)


def get_logger(name: str):
    return logger.bind(name=name)

