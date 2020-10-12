import unittest
from unittest.mock import patch
from search_and_sort_assignment.sort_and_search_list import search_list, sort_list


class MyTestCase(unittest.TestCase):
    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_search_list_when_value_is_in_list(self, mock_list):
        mock_list.return_value = [5, 2, 3]
        expected = 0
        actual = search_list(5)

        self.assertEqual(expected, actual)

    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_search_list_when_value_not_in_list(self, mock_list):
        mock_list.return_value = [5, 2, 3]
        expected = -1
        actual = search_list(6)

        self.assertEqual(expected, actual)

    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_search_list_when_array_contains_string_values(self, mock_list):
        mock_list.return_value = ['a', 'b', 'c']
        expected = 1
        actual = search_list('b')

        self.assertEqual(expected, actual)

    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_sort_list(self, mock_list):
        mock_list.return_value = [5, 2, 3]
        expected = [2, 3, 5]
        actual = sort_list()
        self.assertEqual(expected, actual)

    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_sort_list_with_string_values(self, mock_list):
        mock_list.return_value = ['a', 'e', 'c']
        expected = ['a', 'c', 'e']
        actual = sort_list()
        self.assertEqual(expected, actual)

    @patch('search_and_sort_assignment.sort_and_search_list.make_list')
    def test_sort_list_with_string_and_numeric(self, mock_list):
        mock_list.return_value = [1, 'b', 2]
        with self.assertRaises(TypeError):
            sort_list()


if __name__ == '__main__':
    unittest.main()
