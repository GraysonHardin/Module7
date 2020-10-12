"""
Program: sort_and_search.py
Author: Grayson Hardin
Last date modified: 10/12/2020

"""

from basic_list_exception_assignment.basic_list_exceptions import make_list


def search_list(search_value):
    my_list = (make_list())
    # Below we use a try/catch to raise a value error.
    try:
        index = my_list.index(search_value)
        return index

    except ValueError:  # If the search term is not within the list, it will return a -1
        not_in_list = -1
        return not_in_list


def sort_list():
    my_list = make_list()
    return sorted(my_list)  # I decided to add a return statement to my sort_list so it would not be void. While it could be done with or without, I prefer assigning it to a variable and then returning the variable.


def main():
    user_search_value = int(input("Provide an integer search term: "))  # The list will be searched with this number and will then go to lines 14-20 for validation.
    print(search_list(user_search_value))
    print('This is the sorted list', sort_list())


if __name__ == '__main__':
    main()

