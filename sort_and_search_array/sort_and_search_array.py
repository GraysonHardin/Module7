"""
Program: sort_and_search_array.py
Author: Grayson Hardin
Last date modified: 10/18/2020

This program is nearly the same as the sort and search list assignment, but the key difference is the use of an array.
"""


from basic_list_exception_assignment.basic_list_exceptions import make_list


def search_array(search_value):
    my_array = make_list()
    # Below we use a try/catch to raise a value error.
    try:
        index = my_array.index(search_value)
        return index

    except ValueError:  # If the search term is not within the array, it will return a -1
        not_in_array = -1
        return not_in_array


def sort_array():
  pass

def main():
    user_search_value = int(input("Provide an integer search term: "))  # The array will be searched with this number and will then go to lines 14-20 for validation.
    print(search_array(user_search_value))
    print('This is the sorted array', sort_array())


if __name__ == '__main__':
    main()
