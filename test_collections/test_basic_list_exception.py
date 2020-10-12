import unittest
from unittest.mock import patch
from basic_list_exception_assignment import basic_list_exceptions


class MyTestCase(unittest.TestCase):
    @patch('basic_list_exception_assignment.basic_list_exceptions.get_input', return_value='ab')  # This test handles non-numeric values and will return an error.
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exceptions.make_list()

    @patch('basic_list_exception_assignment.basic_list_exceptions.get_input', return_value='0')  # This test will handle values below 1 and raise an error
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exceptions.make_list()

    @patch('basic_list_exception_assignment.basic_list_exceptions.get_input', return_value='51')  # This test will return an error if the value is too high (above 50).
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exceptions.make_list()




if __name__ == '__main__':
    unittest.main()
