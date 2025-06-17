from itertools import zip_longest

list_numbers = [1, 2, 3, 4, 7, 9, 24, 56]
list_string = ['Firstname', 'Surname', 'Number', 'Email', 'Address', 'Extended information']

for value in zip_longest(list_numbers, list_string):
    print(value)
