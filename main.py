from tools.tools import scrape, add_category
from connection.connection import Connection

# print(scrape())

connection = Connection()
connection2 = Connection()
connection2.close_connection()
data = connection.display_data()
print(data)
connection.close_connection()

