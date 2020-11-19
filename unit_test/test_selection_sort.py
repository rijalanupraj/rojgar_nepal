import unittest
from front_end.company_applicants_page import CompanyApplicants


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        # [user id, user's name, user's phone number, address, job id, job title]
        self.d1 = [4, 'John', '9889889890', 'Kathmandu', 12, 'Developer']
        self.d2 = [12, 'Jack', '9324239890', 'USA', 3, 'Gardener']
        self.d3 = [7, 'Rita', '9423439890', 'Dang', 19, 'Cashier']
        self.data = [self.d1, self.d2, self.d3]

    def test_selection_sort(self):
        """Sorting By name"""
        actual = CompanyApplicants.selection_sort(self.data)
        expect = [self.d2, self.d1, self.d3]
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
