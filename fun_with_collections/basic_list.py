"""
Program: basic_list.py
Author: Grayson Hardin
Last date modified: 10/10/2020


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
