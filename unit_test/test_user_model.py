import unittest
from model.user import *

class Test_User(unittest.TestCase):
    def setUp(self):
        self.user_model1 = User("Anup Rijal", 'anup', '0989098090', 'Dang', 'anup@123')
        self.user_model2 = User("John Brad", 'john', '9932039020', 'California', 'johnIsBeast')
        self.user_model2.set_id('2')

    def test_set_id(self):
        self.user_model1.set_id('1')
        self.assertEqual('1', self.user_model1.get_id())

    def test_get_id(self):
        self.assertEqual('2', self.user_model2.get_id())

    def test_set_name(self):
        self.user_model1.set_name('Anup Raj Rijal')
        self.assertEqual('Anup Raj Rijal', self.user_model1.get_name())

    def test_get_name(self):
        self.assertEqual('John Brad', self.user_model2.get_name())

    def test_set_username(self):
        self.user_model1.set_username('anup1')
        self.assertEqual('anup1', self.user_model1.get_username())

    def test_get_username(self):
        self.assertEqual('john', self.user_model2.get_username())


if __name__ == '__main__':
    unittest.main()
