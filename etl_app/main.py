from etl_app.tools import scrape
from sentry_config import init_sentry

from sqlmodel import SQLModel
from etl_app.db_models import facts_model 
from etl_app.connection import engine, SQLModel
#Always import the models and the connection. SQLModel (table = true) will create a metadata . without the metadata createall doest work.


init_sentry()


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


def main():
    SQLModel.metadata.create_all(engine)
    # data:str = scrape()
    return None

main()


