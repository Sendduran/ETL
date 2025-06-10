from etl_app.db_models.facts_model import Facts
from etl_app.tools.tools import clean_unicode, convert_to_timestamp

class FactService:
    """
    Service class for handling Fact table related database operations.
    """

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def bulk_insert_fact(self, facts_data: list[dict]) -> dict:
        with self.db_connection._get_session() as session:
            for item in facts_data:
                item.update(fact=clean_unicode(item['fact']))
                item.update({"facts_id": convert_to_timestamp(item['created_date'])})
            session.bulk_insert_mappings(Facts, facts_data)
            session.commit()
        return {"message": "Data added to the database successfully"}
