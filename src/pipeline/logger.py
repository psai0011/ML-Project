import logging
import os
from datetime import datetime

# Corrected datetime formatting
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Corrected log directory path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Create only the directory, not the full path with filename

# Corrected log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Fixed basicConfig and formatting
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started.")
