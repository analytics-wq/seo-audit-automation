"""Logging configuration."""
import logging
import colorlog


def setup_logger(level=logging.INFO):
    """Setup colored logger.

    Args:
        level: Logging level
    """
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s',
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    ))

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger
