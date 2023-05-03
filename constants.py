import os

file_path = os.path.realpath(__file__)
directory = r'C:\Users\hp\Desktop\Pythonprogramming\week5\task\data'

PASSWORD = os.path.join(directory, 'password.json') 
ACCEPTED = os.path.join(directory, 'accepted.log') 
FORBIDDEN = os.path.join(directory, 'forbidden.log') 
MEDIUM = os.path.join(directory, 'medium.log') 
STRONG = os.path.join(directory, 'strong.log') 
WEAK = os.path.join(directory, 'weak.log') 

CRITRIA = {
    "length": 8,
    "uppercase": True,
    "lowercase": True,
    "digits": True,
    "special characters": False
}

SLEEP_INTERVAL = 1
MIN_LENGTH = 2
MAX_LENGTH = 9

