from constants import PASSWORD, SLEEP_INTERVAL, MIN_LENGTH, MAX_LENGTH
from check_pass import PasswordChecker
from helper import read_json_file, write_to_json_file
import string
import random
import time


class GeneratePassword:
    def __init__(self):
        self.checker  = PasswordChecker()

    def generatePassword(self):
        """
        Generate random password with random length.
        """
        all_chars = string.ascii_letters + string.digits + string.punctuation.replace("'", "").replace('"', '')
        password = ''.join(random.choice(all_chars)for num in range(random.randint(MIN_LENGTH, MAX_LENGTH)))
 
        return password

    def generatePasswordOnInterval(self, interval):
        """
        """
        sleep_interval = SLEEP_INTERVAL
        start_time = time.time()
        passwords = []

        while (time.time() - start_time) < interval:
            password = self.generatePassword()
            passwords.append(password)
            time.sleep(sleep_interval)

        json_data = read_json_file(PASSWORD)

        for password in passwords:
            json_data['passwords'].append(password)

        write_to_json_file(PASSWORD, json_data)

        self.notify_checker(password_lst=passwords)
        

    def notify_checker(self, password_lst):
        self.checker.check(password_lst)
