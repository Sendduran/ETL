from etl_app.tools import scrape

def test_scrape():
    data = scrape() # calling actual function
    assert isinstance(data, list) # Check if data is a list
    assert len(data) > 0 # Check if data is not empty
    assert all(isinstance(item, dict) for item in data) # Check if all items are dictionaries
