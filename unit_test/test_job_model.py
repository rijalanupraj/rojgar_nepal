import unittest
from model.job import *


class Test_Job(unittest.TestCase):
    def setUp(self):
        self.job_model1 = Job("Developer", "Js developer needed", "20000", "Bachelor Degree", "1")
        self.job_model2 = Job("Gardener", "For mainting the park", "10000", "Grade 5", "2")

    def test_set_title(self):
        self.job_model1.set_title('React Developer')
        self.assertEqual('React Developer', self.job_model1.get_title())

    def test_get_title(self):
        self.assertEqual('Gardener', self.job_model2.get_title())

    def test_set_salary(self):
        self.job_model1.set_salary('100000')
        self.assertEqual('100000', self.job_model1.get_salary())

    def test_get_salary(self):
        self.assertEqual('10000', self.job_model2.get_salary())
