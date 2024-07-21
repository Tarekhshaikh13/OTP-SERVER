# logging_config.py
import logging
import os

def setup_logging():
    # Define the log directory and file
    log_directory = os.getenv('FASTAPI_LOG_CONTAINER')
    os.makedirs(log_directory, exist_ok=True)
    
    log_file = os.path.join(log_directory, 'app.log')

    # Configure logging
    logging.basicConfig(
        filename=log_file,  # Log file location
        level=logging.INFO,  # Log level
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Optionally, add a console handler for immediate output to the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(console_handler)
