import logging
import os
from constants.constants import LOG_DIR, LOG_LEVEL, LOG_FILE_NAME

def create_logger():
    """
    Create a LOGGER to log the application events
    """
    
    # Create a LOGGER
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL)

    # Ensure the logs directory exists
    log_dir = LOG_DIR
    os.makedirs(log_dir, exist_ok=True)

    # Create a file handler
    log_file = os.path.join(log_dir, LOG_FILE_NAME)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(LOG_LEVEL)

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add the file handler to the LOGGER
    logger.addHandler(file_handler)

    return logger

LOGGER = create_logger()