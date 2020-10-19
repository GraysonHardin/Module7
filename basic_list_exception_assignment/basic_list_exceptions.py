"""
Program: basic_list_exceptions.py
Author: Grayson Hardin
Last date modified: 10/12/2020

Like previous examples, this program will print the numbers from user_input. However, if the user_input is outside of the range (less than 1 or greater than 50) it will return a ValueError.
"""
import array as arr


def make_list():
    my_list = arr.array('i', [])  # Note, this has been changed to an array for the sort_and_search_array assignment.
    while len(my_list) <= 2:
        # int function will raise a value exception when it cannot cast to integer.
        user_input = int(get_input())
        if user_input < 1 or user_input > 50:
            raise ValueError

        my_list.append(user_input)

    return my_list


def get_input():
    user_input = input("Enter a number: ")
    return user_input


if __name__ == '__main__':
    example = make_list()
    print(example)

