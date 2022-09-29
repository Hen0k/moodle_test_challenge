import os
from pprint import pprint
from traceback import print_exc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect
from dotenv import load_dotenv

load_dotenv()


# Connect to your PostgreSQL database on a remote server
HOST = os.getenv("DBHOST")
PORT = os.getenv("DBPORT")
USER = os.getenv("DBUSER")
PASS = os.getenv("DBPASS")
DB = os.getenv("DB")

SITES_SCHEMA = "sites_users_schema.sql"
CONNECTION_STR = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}/{DB}"
BANNER = "="*20

# Connect to the database
ENGINE = create_engine(CONNECTION_STR)


# Create the tables
def create_tables():
    try:
        with ENGINE.connect() as conn:
            for name in [SITES_SCHEMA]:
                with open(name) as file:
                    query = text(file.read())
                    conn.execute(query)
                    conn.execute(text('ALTER TABLE "SitesUsers" REPLICA IDENTITY FULL;'))
        print("Successfully created SitesUsers table")
    except:
        print("Unable to create the Table")
        print(print_exc())


# Populate the tables
def insert_data(df: pd.DataFrame, table_name):
    try:
        with ENGINE.connect() as conn:
            df.to_sql(name=table_name, con=conn,
                      if_exists='append', index=False)
        print(f"Done inserting to {table_name}")
        print(BANNER)
    except:
        print("Unable to insert to table")
        print(print_exc())


# Implement Querying functions
def get_table_names():
    with ENGINE.connect() as conn:
        inspector = inspect(conn)
        names = inspector.get_table_names()
        return names


if __name__=="__main__":
    print(get_table_names())