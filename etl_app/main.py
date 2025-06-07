from etl_app.tools import scrape
from sentry_config import init_sentry
from etl_app.connection import DatabaseConnection

############################## Do not delete  ########################################################

# striptime = datetime.strptime("2023-10-02T02:22:00.272Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# print((striptime.timestamp()))
# dt = datetime.now()
# text = dt.isoformat()
# print(text)
# striptime = datetime.strptime(text,"%Y-%m-%dT%H:%M:%S.%f")
# print({":,.6f"}.format(float(striptime.timestamp())))
# print(type(text))
#######################################################################################################################



db_name = "facts_db"
db_user = "postgres"
db_password = "admin"
db_server = "localhost"
db_port = 5432

def main():    
    init_sentry()
    # scrape()
    db = DatabaseConnection(db_name, db_user, db_password, db_server, db_port)
    db.create_db_and_tables()
    

if __name__ == "__main__":
    main()




