import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Set up logger
logger = logging.getLogger("stock-ai-logger")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File handler with rotation
file_handler = RotatingFileHandler("logs/app.log", maxBytes=5_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)

# Formatter for log messages
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
