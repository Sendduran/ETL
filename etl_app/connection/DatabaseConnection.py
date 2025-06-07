import psycopg2
from sqlmodel import create_engine, SQLModel, Session
from etl_app.db_models import facts_model # Facts model has the metadata of the fact table created. 


class DatabaseConnection:
    def __init__(self, db_name, db_user, db_password, db_server, db_port):       
        self.db_url = f'postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}'
        self.engine = create_engine(self.db_url, echo = True)  # echo - It will make the engine print all the sql statements it executes


    
    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine) # metadata of the table is needed to create the table

    def create_session(self): 
        with Session(self.engine) as session:
            yield session



    