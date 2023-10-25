import logging


def get_custom_logger(name, log_level=logging.INFO):
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
