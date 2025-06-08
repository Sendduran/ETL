from etl_app.tools import scrape , bulk_insert_fact
from sentry_config import init_sentry
from etl_app.connection import DatabaseConnection

db_name = "facts_db"
db_user = "postgres"
db_password = "admin"
db_server = "localhost"
db_port = 5432

def main():    
    init_sentry()
    facts_data =  scrape()
    db = DatabaseConnection(db_name, db_user, db_password, db_server, db_port)
    db.create_db_and_tables()    
    bulk_insert_fact(facts_data , db.get_session())
    
if __name__ == "__main__":
    main()