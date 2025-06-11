from datetime import datetime
import requests

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

    reponse = requests.get("https://raw.githubusercontent.com/vetstoria/random-k9-etl/refs/heads/main/source_data.json")
    reponse.raise_for_status()  # Ensure we got a successful response
    json_data:list[dict] = reponse.json()

    return json_data
