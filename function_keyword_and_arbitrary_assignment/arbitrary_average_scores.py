"""
Program: arbitrary_average_scores.py
Author: Grayson Hardin
Last date modified: 10/12/2020

This program can take a infinite amount of numbers, names, etc. It will then return the GPU (average of the numbers previously entered) and then return the course name.
"""


def average_scores(*args, **kwargs):
    output = ''
    average = round(sum(args) / len(args), 2)  # Calculation

    for key, value in kwargs.items():
        output += f' {key} = {value}'
    return f'Results:{output} with current average {average}'  # Formatted string


def main():
     # From what I could understand, the assignment was wanting various examples to show that keyword arguments can take as many values as needed. Thus, I added a few different scenarios.
    print(average_scores(4, 3, 2, 4, 8, 7, 10, 13, 1, 6, name='Grayson', gpa='4.0', course='Python'))  # There is an infinite number of values that key arguments can take. i.e; 1 or 1,000.
    print(average_scores(4, 3, 2, 4, name='John', course='History'))  # Here is another scenario with four numbers and two keywords.
    print(average_scores(4, 3, name='Taylor'))  # Here is another scenario withe ven less key arguments.


if __name__ == '__main__':
    main()
