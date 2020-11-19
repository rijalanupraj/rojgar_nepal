import unittest
from back_end.connection import *

class TestDbConnection(unittest.TestCase):
    def setUp(self):
        self.dbconnect = DbConnection()
    def test_insert(self):
        query = "INSERT into user (`name`, `username`, `phone`,`address`,`password`) VALUES (%s,%s,%s,%s,%s);"
        values = ('Ram','ram32','9876538902','Dhading-5','Ram@321')
        self.dbconnect.insert(query,values)
        expect = [('Ram','ram32','9876538902','Dhading-5','Ram@321')]
        actual = self.dbconnect.select("SELECT name,username,phone,address,password FROM user WHERE username='ram32'")
        self.assertEqual(expect,actual)
    def test_update(self):
        query = "UPDATE user set `name`=%s,`phone`=%s,`address`=%s,`password`=%s WHERE username=%s;"
        values = ('Ram','9877838912','Dhading-9','Ram@3210','ram32')
        self.dbconnect.update(query,values)
        expect =[('Ram','ram32','9877838912','Dhading-9','Ram@3210')]
        actual = self.dbconnect.select("SELECT name,username,phone,address,password FROM user WHERE username='ram32'")
        self.assertEqual(expect,actual)
    def test_delete(self):
        query="DELETE from user WHERE username=%s"
        values=('ram32',)
        self.dbconnect.delete(query,values)
        expect = []
        actual = self.dbconnect.select("SELECT name,username,phone,address,password FROM user WHERE username='ram32'")
        self.assertEqual(expect,actual)
    def test_select(self):
        query = "INSERT into user (`name`, `username`, `phone`,`address`,`password`) VALUES (%s,%s,%s,%s,%s);"
        values = ('John','john','9793029021','Texas','JohnIsBeast')
        self.dbconnect.insert(query,values)
        expect = [('John','john','9793029021','Texas','JohnIsBeast')]
        actual = self.dbconnect.select("SELECT name,username,phone,address,password FROM user WHERE username='john'")
        self.assertEqual(expect,actual)

if __name__ == '__main__':
    unittest.main()
