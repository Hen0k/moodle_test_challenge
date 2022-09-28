from typing import Dict, Union
from datetime import datetime, timedelta
from faker import Faker
from pprint import pprint
import pandas as pd
from postgress_manager import create_tables, insert_data
from random import randint
import time

fake = Faker(use_weighting=True)
# Faker.seed(4321)

"""
- user_handle
- **admin_email**
- registration_timestamp
"""

def generate_sites_users(users_count:int=1, start_date: datetime.date=None) -> Dict[str, Union[str, datetime.date]]:
    """This will generate users as a dictionary holding the following properties:
    - username
    - full name
    - admin_email
    - registration_timestamp
    """
    if not start_date:
        start_date = datetime(year=2008, month=1, day=1)    # Assuming moodle started the site in 2008
    for _ in range(users_count):
        username, fullname, _, _, admin_email, _ = fake.simple_profile().values()
        reg_timestamp = fake.date_time_between(start_date=start_date).timestamp()
        yield {
            "username": username,
            "fullname": fullname,
            "admin_email": admin_email,
            "registration_timestamp": reg_timestamp
        }


def populate_table(count: int=1, start_date: datetime.date=None):
    sites_users = [*generate_sites_users(users_count=count, start_date=start_date)]
    df = pd.DataFrame(sites_users)
    create_tables()
    insert_data(df, table_name="SitesUsers")


def add_new_users():
    count = randint(0, 50)
    start_date = datetime.now() - timedelta(days=1)
    populate_table(users_count=count, start_date=start_date)



if __name__ == "__main__":
    populate_table(users_count=100, start_date=datetime(year=2010, month=1, day=1 ))
    while True:
        add_new_users()
        time.sleep(86400) # 1 day
