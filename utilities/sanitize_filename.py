import logging
import os

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure the logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create a file handler
log_file = os.path.join(log_dir, "application.log")
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Create a formatter and set it for the file handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


def sanitize_filename(filename):
    """
    Sanitize the filename to remove any invalid characters \n
    params: filename: str: The filename to sanitize \n
    \n
    returns: str: The sanitized filename
    """
    logger.debug(f"Sanitizing filename: {filename}")
    sanitized_filename = filename.replace(",", "")
    return sanitized_filename
