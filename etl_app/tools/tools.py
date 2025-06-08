import json
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from etl_app.db_models.facts_model import Facts
from  etl_app.connection import DatabaseConnection
from sqlmodel import Session
from datetime import datetime

current_dir:str = os.path.dirname(__file__)
file_path: str = os.path.join(current_dir, '../data/sample.json')

def clean_unicode(uncleaned_strting: str) -> str:    
    try:
         cleaned_string = uncleaned_strting.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
    except UnicodeEncodeError:
        pass
    return cleaned_string

# def add_category(data_list:list[dict])->list[dict]:
#     for item in data_list:
#         is_con_no:bool = True if re.search(r"\d+",item["fact"]) else False
#         item.update({"has_no":is_con_no})
#     return data_list

# # Checks for number in the given string and returns a bool
# def check_for_no(fact:str)-> bool:
#     has_no:bool  = True if re.search(r"\d+", fact) else False
#     return has_no

#converts the given the string to timestamp
def convert_to_timestamp(time:str)-> int:
    striptime: str  = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(float(striptime.timestamp())*1000000)

def scrape():
    driver=webdriver.Firefox()
    driver.get("https://raw.githubusercontent.com/vetstoria/random-k9-etl/refs/heads/main/source_data.json")
    elem  = driver.find_element(By.TAG_NAME, "body")
    body:str = elem.get_attribute('innerText')
    json_data:list[dict] = json.loads(body)
    cleaned_data:list[dict] = clean_unicode(json_data)
    driver.close()
    return cleaned_data

def bulk_insert_fact(facts_data:list[dict] , session:Session):
    facts = []
    for item in facts_data:
        item.update(fact = clean_unicode(item['fact']))
        item.update({"facts_id": convert_to_timestamp(item['created_date'])})
        # print(item)
        facts.append(item)  
    # print(facts)
    session.bulk_insert_mappings(Facts, facts)
    session.commit()