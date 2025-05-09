import random

#1
def print_numb_with_if(x):
    if type(x) is int:
        print(f'{x}'*30)
    elif type(x) is tuple:
        print(random.randint(x[0], x[1]))


print("\nZadanie 1")
print_numb_with_if(1)
print_numb_with_if((0, 30))
print("-"*30)


#2
def print_numb_with_match_case(x):
    match x:
        case 1:
            print(f'{x}' * 30)
        case (0,30):
            print(random.randint(x[0], x[1]))

print("\nZadanie 2")
print_numb_with_match_case(1)
print_numb_with_match_case((0, 30))
print("-"*30)

#3
def print_numb_with_match_case_dictionary(x: dict):
        match x:
            case {"number1": 1}:
                print(f'{x["number1"]}' * 30)
            case {"number1": (0,30)}:
                print(random.randint(list(x.get('number1'))[0], list(x.get('number1'))[1]))

print("\nZadanie 3")
print_numb_with_match_case_dictionary({"number1": 1})
print_numb_with_match_case_dictionary({"number1": (0, 30)})
print("-"*30)


#4
def print_numb_with_ternar(x):
    print(f'{x}'*30) if type(x) is int else print(random.randint(x[0], x[1]))

print("\nZadanie 4")
print_numb_with_ternar(1)
print_numb_with_ternar((0, 30))
print("-"*30)
"""""
Алгоритм:
Если на вход подали 1 - Напечатать строку, состояющую из 30-ти символов "1"
Если на вход подали tuple(0, 30) - Напечатать псевдорандомное целое число в пределах от 0 до 30

---
1) Реализовать данный алгоритм с помощью if-elif-else конструкции
2) Реализовать данный алгоритм с помощью match-case конструкции
3) Реализовать данный алгоритм с помощью match-case реализованного с помощью словаря
4) Реализовать данный алгоритм с помощью тернарного оператора
"""""