import sys
from loguru import logger

# Filled with all of the default values for the config. Automatically includes
logger.remove()
logger.add(sys.stderr, enqueue=True)
