import json
from selenium import webdriver
from selenium.webdriver.common.by import By
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
