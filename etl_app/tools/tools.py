import json
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir:str = os.path.dirname(__file__)
file_path: str = os.path.join(current_dir, '../data/sample.json')

def clean_unicode(data_list: list[dict]) -> list[dict]:
    for item in data_list:
        for key, value in item.items():
            if isinstance(value, str):
                try:
                    item[key] = value.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
                except UnicodeEncodeError:
                    pass
    return data_list

def add_category(data_list:list[dict])->list[dict]:
    for item in data_list:
        is_con_no:bool = True if re.search(r"\d+",item["fact"]) else False
        item.update({"has_no":is_con_no})
    return data_list


def scrape():
    driver=webdriver.Firefox()
    driver.get("https://raw.githubusercontent.com/vetstoria/random-k9-etl/refs/heads/main/source_data.json")
    elem  = driver.find_element(By.TAG_NAME, "body")
    body:str = elem.get_attribute('innerText')
    json_data:list[dict] = json.loads(body)
    cleaned_data:list[dict] = clean_unicode(json_data)
    driver.close()
    return cleaned_data
