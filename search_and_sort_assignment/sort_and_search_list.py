"""
Program: sort_and_search.py
Author: Grayson Hardin
Last date modified: 10/11/2020


"""

from basic_list_exception_assignment.basic_list_exceptions import make_list


def search_list(search_value):
    my_list = (make_list())
    # Below we use a try/catch to raise a value error.
    try:
        index = my_list.index(search_value)
        return index

    except ValueError:
        not_in_list = -1
        return not_in_list


def sort_list():
    pass


def main():
    user_search_value = int(input("Provide an integer search term: "))
    print(search_list(user_search_value))
    print('This is the sorted list', sort_list())


if __name__ == '__main__':
    main()
