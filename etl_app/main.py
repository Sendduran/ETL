from etl_app.tools import scrape
from etl_app.connection import Connection
from .sentry_config import init_sentry


init_sentry()

a = 1/0

def main():
    data:str = scrape()
    return data

main()
