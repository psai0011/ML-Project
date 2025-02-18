import sys
import logging

# Set up logging for both console & file output
log_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

file_handler = logging.FileHandler("error.log")
file_handler.setFormatter(log_formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, console_handler]  # ✅ Only handlers specified
)

def error_message_detail(error, error_detail):
    """Extracts detailed error information including filename and line number."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    return f"Error occurred in Python file [{file_name}] at line number [{exc_tb.tb_lineno}]: {str(error)}"

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 0 / 1  # Intentional error
    except Exception as e:
        logging.exception("An exception occurred")  # Logs traceback automatically
        raise CustomException(e, sys)  # Raising with details
