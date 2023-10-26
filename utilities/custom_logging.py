import logging

def clear_custom_log_file():
    with open('my_custom.log', 'w'):
        pass  # This will clear the file by opening it in write mode and immediately closing it

def get_custom_logger(name, log_level=logging.INFO):
    # Clear the log file before configuring the logger
    clear_custom_log_file()

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler('my_custom.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
