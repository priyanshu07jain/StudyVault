import logging
import os
# Ensure the data directory exists before logging starts
os.makedirs('data', exist_ok=True)
logging.basicConfig(
filename='data/logs.txt',
level=logging.INFO,
format='%(asctime)s | %(levelname)-8s | %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)


# Also print INFO+ to the terminal during development
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)



logging.getLogger().addHandler(console_handler)
def log(message: str, level: str = 'info') -> None:
    """
    Log a message at the specified level.
    Args:
    message: The text to log.
    level: One of 'info', 'warning', 'error', 'debug'.
    """
    level = level.lower()
    if level == 'debug':
        logging.debug(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.info(message)
