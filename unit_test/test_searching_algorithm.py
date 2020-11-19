import unittest
from front_end.user_job_page import UserJob
from model.job import Job


class TestSearch(unittest.TestCase):

    def setUp(self):
        d1 = ['1', 'Gardener', 'Work in park', '7000', 'Grade 5', 'KTM Central Park']
        d2 = ['4', 'Developer', 'Who have good knowledge of both front and backend', '20000', 'Bachelor',
              'Kwality Resturant']
        d3 = ['3', 'Cashier', 'Deposit and withdraw cash at bank', '10000', 'Grade 12', 'Nabil Bank']
        self.data = [d1, d2, d3]

    def test_search_algo(self):
        search_by1 = 'Job Title'
        search_text1 = 'Developer'
        expect1 = [['4', 'Developer', 'Who have good knowledge of both front and backend', '20000', 'Bachelor',
                    'Kwality Resturant']]
        actual1 = UserJob.searching_algo(self.data, search_by1, search_text1)
        self.assertEqual(actual1, expect1)

        search_by2 = 'Company Name'
        search_text2 = 'nabil bank'
        expect2 = [['3', 'Cashier', 'Deposit and withdraw cash at bank', '10000', 'Grade 12', 'Nabil Bank']]
        actual2 = UserJob.searching_algo(self.data, search_by2, search_text2)
        self.assertEqual(actual2, expect2)


if __name__ == '__main__':
    unittest.main()
