from runpy import run_path


def ex6_1():
    return [x for x in range(1, 1001) if x % 7 == 0]


def ex6_2():
    numbers_7 = ex6_1()
    return [x if x % 3 == 0 else f'{x}'*2 for x in numbers_7]


def ex6_3():
    string_with_spaces = "  hel l o      world   "
    return len([value for value in tuple(string_with_spaces) if value == ' '])


def ex6_4():
    string_words = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
    string_words = string_words.split()
    return [word for word in string_words if word[0].lower() == 'y']


def ex6_5():
    string1 = "hi, 3.44, 535  "
    #list_indexes = tuple((index, value) for index, value in zip(string1.split(), [x for x in range(1, 4)]))
    list_indexes = [(index, value) for index, value in enumerate(string1.split())]
    return (list_indexes)


def ex6_6():
    string_words = "In 1984 there were 13 instances of a protest with over 1000 people attending"
    return list(word for word in string_words.split() if word.isdigit())


def ex6_7():
    return ['четное' if x % 2 == 0 else 'нечетное' for x in range(1, 21)]


def ex6_8():
    string_words = "The trickiest part of learning list comprehension for me was really understanding the syntax."
    return [word for word in string_words.split() if len(word) < 4]


def ex6_9():
    return [x for x in range(1, 51) if x != 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]


print("Задание 1: ", ex6_1())
print("Задание 2: ", ex6_2())
print("Задание 3: ", ex6_3())
print("Задание 4: ", ex6_4())
print("Задание 5: ", ex6_5())
print("Задание 6: ", ex6_6())
print("Задание 7: ", ex6_7())
print("Задание 8: ", ex6_8())
print("Задание 9: ", ex6_9())
