from sqlmodel import create_engine, SQLModel, Session
from etl_app.db_models import facts_model # Facts model has the metadata of the fact table created.
from urllib.parse import quote_plus
from etl_app.tools.tools import clean_unicode, convert_to_timestamp
from etl_app.db_models.facts_model import Facts

class DatabaseConnection:
    """
    Handles connection to a PostgreSQL database and provides methods
    for creating tables and bulk inserting data.
    """

    def __init__(self, db_name, db_user, db_password, db_server, db_port):
        """
        Initialize the database connection.

        Args:
            db_name (str): Name of the database.
            db_user (str): Database user.
            db_password (str): Database password.
            db_server (str): Database server address.
            db_port (str/int): Database server port.
        """
        self.db_url: str = f'postgresql://{db_user}:{quote_plus(db_password)}@{db_server}:{db_port}/{db_name}'
        self.engine = create_engine(self.db_url, echo = True)  # echo - It will make the engine print all the sql statements it executes

    def create_db_and_tables(self):
        """
        Create all tables in the database as defined in the SQLModel metadata.
        """

        SQLModel.metadata.create_all(self.engine) # metadata of the table is needed to create the table

    def bulk_insert_fact(self, facts_data: list[dict]) -> dict:

        with self._get_session() as session:
            for item in facts_data:
                item.update(fact=clean_unicode(item['fact']))
                item.update({"facts_id": convert_to_timestamp(item['created_date'])})
            session.bulk_insert_mappings(Facts, facts_data)
            session.commit()
        return {"message": "Data added to the database successfully"}

    def _get_session(self) -> Session:
        return Session(self.engine)
