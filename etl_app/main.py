from etl_app.tools import scrape , bulk_insert_fact
from sentry_config import init_sentry
from etl_app.connection import DatabaseConnection

############################## Do not delete  ########################################################


#######################################################################################################################



db_name = "facts_db"
db_user = "postgres"
db_password = "admin"
db_server = "localhost"
db_port = 5432

def main():    
    # init_sentry()
    # # scrape()
    db = DatabaseConnection(db_name, db_user, db_password, db_server, db_port)
    db.create_db_and_tables()
    facts_data = [{"fact": "Heres looking at you. Dogs have three eyelids, an upper lid, a lower lid and the third lid, called a nictitating membrane or \"haw,\" which helps keep the eye moist and protected.",
    "created_date": "2023-10-02T02:22:00.272Z"},{"fact": "Dogs are direct descendants of wolves.", "created_date": "2024-05-12T08:17:49.657Z"}]
    bulk_insert_fact(facts_data , db.get_session())
    

if __name__ == "__main__":
    main()