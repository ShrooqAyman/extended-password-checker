from InvalidPasswordError import InvalidPasswordError
from constants import CRITRIA
from helper import classify_password

class Checker:

    def check(self):
        pass

class PasswordChecker(Checker):

    def check(self, password_lst):
        """
        Check strength for all passwords in password_lst and classify to strong, weak, forbidden, accepted or medium log file.
        
        Args:
            password_lst(list): list of passwords
        
        """
        for password in password_lst:
            errors_lst = []
            
            if len(password) < CRITRIA['length']:
                errors_lst.append(f'The password must contain at least {CRITRIA["length"]} characters.')

            if any(char.isupper() for char in password) != CRITRIA['uppercase']:
                errors_lst.append('The password must contain at least one uppercase letter.')

            if any(char.islower() for char in password) != CRITRIA['lowercase']:
                errors_lst.append('The password must contain at least one lowercase letter.')

            if any(char.isdigit() for char in password) != CRITRIA['digits']:
                errors_lst.append('The password must contain at least one digit.')

            classify_password(password, errors_lst)

                