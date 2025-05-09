def add_pristavka_for_element_in_list(element: str):
    return element + '_'


list_string = ['1234а', 'Teаst', 'а_telegram']
list_string = list(map(add_pristavka_for_element_in_list, list_string))
sorted_a_list_string = [value for value in list_string if value[0]== 'а']
print(sorted_a_list_string)