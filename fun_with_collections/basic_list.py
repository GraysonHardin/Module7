"""
Program: basic_list.py
Author: Grayson Hardin
Last date modified: 10/12/2020

This program takes inputs and then returns the list in the order that was given.
"""


def make_list():
    my_list = []

    while len(my_list) <= 2:
        # int function will raise a value exception when it cannot cast to integer.
        user_input = int(get_input())

        my_list.append(user_input)

    return my_list


def get_input():
    user_input = input("Enter a number: ")
    return user_input


if __name__ == '__main__':
    list_of_items = make_list()
    print(list_of_items)
