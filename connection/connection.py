import psycopg2

class Connection:
    def __init__(self):
        self.connect = psycopg2.connect("dbname=facts_db user=postgres password=admin")
        self.cursor = self.connect.cursor()


    def display_data(self):
        self.cursor.execute("Select * from sample_table")
        data = self.cursor.fetchall()
        return data

    def close_connection(self):
        self.connect.close()
