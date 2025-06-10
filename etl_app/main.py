from etl_app.tools import scrape
from etl_app.sentry_config import init_sentry
from etl_app.connection import DatabaseConnection
from dotenv import load_dotenv
import os
load_dotenv()

db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_server = os.getenv("db_server")
db_port = os.getenv("db_port")

def main():
    init_sentry()
    facts_data =  scrape()
    db = DatabaseConnection(db_name, db_user, db_password, db_server, db_port)
    db.create_db_and_tables()
    db.bulk_insert_fact(facts_data)


if __name__ == "__main__":
    main()
