from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.tools import clean_unicode
import json


driver = webdriver.Firefox()
driver.get("https://raw.githubusercontent.com/vetstoria/random-k9-etl/refs/heads/main/source_data.json")
elem = driver.find_element(By.TAG_NAME, "body")
body = elem.get_attribute('innerText')
json_data = json.loads(body)
cleaned_data = clean_unicode(json_data)

with open("data/sample.json", "w", encoding='utf-8') as file:
    json.dump(cleaned_data, file)

driver.close()

