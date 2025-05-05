import json
import re 
import os 

current_dir:str = os.path.dirname(__file__)  
file_path: str = os.path.join(current_dir, '../data/sample.json')

with open(file_path, 'r') as file:
    data_txt:list[dict] = json.load(file)

def clean_unicode(data_list: list[dict]) -> list[dict]:
    for item in data_list:
        for key, value in item.items():
            if isinstance(value, str):
                try:
                    item[key]:str = value.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
                except UnicodeEncodeError:
                    pass
    return data_list

def add_category(data_list:list[dict])->list[dict]:
    for item in data_list:
        is_con_no:bool = True if re.search(r"\d+",item["fact"]) else False
        item.update({"is_no":is_con_no})
    return data_list


modified_data = add_category(clean_unicode(data_txt))
with open(file_path, 'w') as file:
    json.dump(modified_data, file, indent=4)