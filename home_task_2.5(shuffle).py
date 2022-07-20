# 5.Реализуйте алгоритм перемешивания списка. (Методом shuffle)

import random

list_length = int(input('Enter the desired number of list items = '))
original_list = list()

for i in range(list_length):
    original_list.append(input(f'Enter a number № {i + 1} --> '))

print('You have set a list -->', original_list)

random.shuffle(original_list)
print('List after mixing --> ', original_list)
