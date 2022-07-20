# 5.Реализуйте алгоритм перемешивания списка.(Алгоритм перемешивания Фишера-Йейтса)

import random

list_length = int(input('Enter the desired number of list items = '))
original_list = list()

for i in range(list_length):
    original_list.append(input(f'Enter a number № {i + 1} --> '))

print('You have set a list -->', original_list)

for i in range(len(original_list) - 1, 0, -1):
    j = int(random.randint(0, i + 1))
    original_list[i], original_list[j] = original_list[j], original_list[i]

print('List after mixing --> ', original_list)