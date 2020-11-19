import mysql.connector
from mysql.connector import Error

class DbConnection:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost', user='root', password='root', database='rojgarnepal')
            if self.con.is_connected():
                self.cursor = self.con.cursor()
        except Error:
            print('Error While connecting. Check your database.', Error)
    def insert(self, query, values):
        try:
            if self.con.is_connected():
                self.cursor.execute(query, values)
                self.con.commit()
        except:
            print("Error while inserting into table")
    def update(self, query, values):
        try:
            if self.con.is_connected():
                self.cursor.execute(query, values)
                self.con.commit()
        except:
            print("Error while updating database")
    def delete(self, query, values):
        try:
            if self.con.is_connected():
                self.cursor.execute(query, values)
                self.con.commit()
        except:
            print("Error while deleting.")
    def select(self, query):
        try:
            if self.con.is_connected():
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                self.con.commit()
                return records
        except:
            print("Error while reading database.")
