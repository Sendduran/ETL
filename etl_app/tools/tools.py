import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from etl_app.db_models.facts_model import Facts
from  etl_app.connection import DatabaseConnection
from sqlmodel import Session
from datetime import datetime

def clean_unicode(uncleaned_strting: str) -> str:    
    try:
         cleaned_string = uncleaned_strting.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
    except UnicodeEncodeError:
        pass
    return cleaned_string

#converts the given the string to timestamp
def convert_to_timestamp(time:str)-> int:
    striptime: str  = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(float(striptime.timestamp())*1000000)

def scrape()-> list[dict]:
    driver=webdriver.Firefox()
    driver.get("https://raw.githubusercontent.com/vetstoria/random-k9-etl/refs/heads/main/source_data.json")
    elem  = driver.find_element(By.TAG_NAME, "body")
    body:str = elem.get_attribute('innerText')
    json_data:list[dict] = json.loads(body)
    driver.close()
    return json_data

def bulk_insert_fact(facts_data:list[dict] , session:Session) -> dict:
    for item in facts_data:
        item.update(fact = clean_unicode(item['fact'])) # update the dictionary with clened fact
        item.update({"facts_id": convert_to_timestamp(item['created_date'])})     # create a new key "facts_id" based on the created_date  
    session.bulk_insert_mappings(Facts, facts_data) # sqlalchemy module to input multiple data at once
    session.commit() #commit the data to the database
    session.close() # close the session
    return {"message": "Data added to the database successfully"}