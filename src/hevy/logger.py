"""Logging configuration for the project."""

import logging
import sys
from datetime import datetime

from .config import config


def setup_logger(
    name: str = config.PROJECT_NAME,
    level: str | None = None,
    log_to_file: bool = True,
) -> logging.Logger:
    """
    Set up logger that writes to both stdout and log files.

    Args:
        name: Logger name (default: project name)
        level: Logging level (default: from config)
        log_to_file: Whether to log to file (default: True)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Set logging level
    log_level = level or config.LOG_LEVEL
    logger.setLevel(getattr(logging, log_level.upper()))

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - "
        "%(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    simple_formatter = logging.Formatter("%(levelname)s - %(message)s")

    # Console handler (stderr, so it never pollutes piped command output)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(getattr(logging, config.LOG_CONSOLE_LEVEL.upper()))
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)

    # File handler (log directory)
    if log_to_file:
        config.LOG_DIR.mkdir(exist_ok=True)

        log_filename = f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
        log_path = config.LOG_DIR / log_filename

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)

    return logger


# Default logger instance
logger = setup_logger()
