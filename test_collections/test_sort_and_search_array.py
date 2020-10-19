import unittest
from unittest.mock import patch
import array as arr
from sort_and_search_array.sort_and_search_array import search_array, sort_array


class MyTestCase(unittest.TestCase):

    @patch('sort_and_search_array.sort_and_search_array.make_list')
    def test_search_array_when_value_is_in_array(self, mock_list):
        mock_list.return_value = arr.array('i', [5, 2, 3])
        expected = 0
        actual = search_array(5)

        self.assertEqual(expected, actual)

    @patch('sort_and_search_array.sort_and_search_array.make_list')
    def test_search_array_when_value_not_in_array(self, mock_list):
        mock_list.return_value = arr.array('i', [5, 2, 3])
        expected = -1
        actual = search_array(6)

        self.assertEqual(expected, actual)

    @patch('sort_and_search_array.sort_and_search_array.make_list')
    def test_search_list_when_array_contains_string_values(self, mock_list):
        mock_list.return_value = arr.array('u', ['a', 'b', 'c'])
        expected = 1
        actual = search_array('b')

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
