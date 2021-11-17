import random
import string
from datetime import datetime
from time import sleep

random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '-' , k = 30))

while True:
    now = datetime.now()
    fnow = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(f"{fnow}: {random_string}")
    sleep(5)
