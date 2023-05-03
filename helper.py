import logging
import json
from constants import STRONG, MEDIUM, FORBIDDEN, WEAK, ACCEPTED


def create_log_file(file_name, logg):
    """
    Creates a log file and sets up a logger object to log messages.

    Args:
        file_name (str): name of the log file to be created.
        logger (str): name of the logger object.

    Returns:
        logger: logger object set up to log messages.
    """ 
    logger = logging.getLogger(logg)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(file_name)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


forbidden = create_log_file(FORBIDDEN, 'forbidden')
weak = create_log_file(WEAK, 'weak')
medium = create_log_file(MEDIUM, 'medium')
accepted = create_log_file(ACCEPTED, 'accepted')
strong = create_log_file(STRONG, 'strong')


def classify_password(password, error_lst):
    count_errors = len(error_lst)
    if count_errors == 0:
        global strong
        strong.info(password)
    elif count_errors == 1:
        global accepted
        accepted.info(password)
    elif count_errors == 2:
        global medium
        medium.info(password)
    elif count_errors == 3:
        global weak
        weak.info(password)
    elif count_errors == 4:
        global forbidden
        forbidden.info(password)


def read_json_file(file):
    try:
        with open(file, 'r') as f:
            try:
                json_data = json.load(f)
                return json_data
            except json.JSONDecodeError as e:
                print(e)
    except FileNotFoundError as e:
        print(e)


def write_to_json_file(file, data):
    try:
        with open(file, 'w') as file:
            json.dump(data, file)
    except FileNotFoundError as e:
        print(e)
