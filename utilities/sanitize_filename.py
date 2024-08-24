from create_logger.logger import LOGGER

logger = LOGGER


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
