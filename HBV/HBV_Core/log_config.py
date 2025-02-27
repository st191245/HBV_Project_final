from HBV_Core.user_config import *
import logging


# Authored by:Shunmuga Priya
def setup_logger(name, log_file, level=logging.INFO):
    """
    Configures a logger to write log messages to a specified file.

    :param name: Name of the logger (e.g., 'action', 'warning', 'error').
    :param log_file: Path to the log file.
    :param level: The minimum log level to capture (default is INFO).
    :return: Configured logger object.
    """
    # Create a file handler to write logs to the specified log file with UTF-8 encoding
    handler = logging.FileHandler(log_file, encoding="utf-8")

    # Define the log message format (timestamp, logger name, log level, and message)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)  # Set the format for the handler

    # Create and configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)  # Set the log level (e.g., INFO, WARNING, ERROR)
    logger.addHandler(handler)  # Add the handler to the logger

    return logger


# logfile paths
ACTION_LOG_FILE = os.path.join(BASE_PATH, "actions.log")  # Log file for action-related logs
WARNING_LOG_FILE = os.path.join(BASE_PATH, "warnings.log")  # Log file for warning logs
ERROR_LOG_FILE = os.path.join(BASE_PATH, "errors.log")  # Log file for error logs

# Create separate loggers for different log types
action_logger = setup_logger("action", ACTION_LOG_FILE, logging.INFO)  # Logger for infos
warning_logger = setup_logger("warning", WARNING_LOG_FILE, logging.WARNING)  # Logger for warnings
error_logger = setup_logger("error", ERROR_LOG_FILE, logging.ERROR)  # Logger for errors
