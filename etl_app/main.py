from etl_app.tools import scrape
from etl_app.connection import Connection

def main():
    data:str = scrape()
    return data

