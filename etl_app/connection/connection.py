import psycopg2
from sqlmodel import create_engine, SQLModel

db_name = "facts_db"
db_user = "postgres"
db_password = "admin"
db_server = "localhost"
db_port = 5432



db_url = f'postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}'

engine = create_engine(db_url, echo = True)  # echo - It will make the engine print all the sql statements it executes

# class Connection:
#     def __init__(self):
#         self.connect = psycopg2.connect("dbname=facts_db user=postgres password=admin")
#         self.cursor = self.connect.cursor()


#     def display_data(self):
#         self.cursor.execute("Select * from sample_table")
#         data = self.cursor.fetchall()
#         return data

#     def close_connection(self):
#         self.connect.close()

