list_numbers = [1,2,3,4,7,9]
list_string = ['Firstname', 'Surname', 'Number', 'Email', 'Address', 'Extended information']

for i, j in zip(list_numbers, list_string):
    print(i, j)