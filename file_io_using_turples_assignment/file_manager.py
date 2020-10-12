"""
Program: file_manager.py
Author: Grayson Hardin
Last date modified: 10/12/2020

This will generate a txt file, write to it, close, and print the values (that were given on the txt file) to the console.

As a side note, this was a little tricky but was fun. Interesting to see how Python can export and return values.
"""


def write_to_file(values):
    f = open("student_info.txt", "a")  # Here the file name is defined

    for value in values:  # I decided to go with a for loop
        f.write(f'{value} ')
    f.write('\n')
    f.close()  # Closes the txt file


def read_from_file():  # This reads the txt file
    f = open("student_info.txt", "r")
    print(f.read())


def get_student_info(**kwargs):
    output = ''

    for key, value in kwargs.items():
        output += f'{value} '
    my_tuple = (output,)

    continue_getting_test_scores = True

    while continue_getting_test_scores:
        user_test_score_input = input('Enter test scores. To end, type "End" ')  # Re-evaluate whether to continue looping

        if user_test_score_input == 'End':
            continue_getting_test_scores = False

        else:
            my_tuple += (user_test_score_input,)

    write_to_file(my_tuple)


def main():
    continue_getting_test_scores = True

    while continue_getting_test_scores:
        student_first_name = input("Enter first name: ")  # Gain Input
        student_last_name = input("Enter last name: ")  # Gain Input

        if student_first_name == 'End' or student_last_name == 'End':
            continue_getting_test_scores = False

        else:
            get_student_info(first_name=student_first_name, last_name=student_last_name)


if __name__ == '__main__':
    main()
    read_from_file()
