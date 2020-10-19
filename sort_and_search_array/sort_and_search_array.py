"""
Program: sort_and_search_array.py
Author: Grayson Hardin
Last date modified: 10/12/2020

This program is nearly the same as the sort and search list assignment, but the key difference is the use of an array.
"""


from basic_list_exception_assignment.basic_list_exceptions import make_list


def search_array(search_value):
   pass

def sort_array():
  pass

def main():
    user_search_value = int(input("Provide an integer search term: "))  # The array will be searched with this number and will then go to lines 14-20 for validation.
    print(search_array(user_search_value))
    print('This is the sorted array', sort_array())


if __name__ == '__main__':
    main()
