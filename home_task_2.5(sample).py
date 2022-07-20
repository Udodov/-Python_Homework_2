# 5.Реализуйте алгоритм перемешивания списка.(С помощью функции sample (c сохранением исходного списка))

import random

list_length = int(input('Enter the desired number of list items = '))
original_list = list()

for i in range(list_length):
    original_list.append(input(f'Enter a number № {i + 1} --> '))

print('You have set a list -->', original_list)

mixing_list = random.sample(original_list, len(original_list))
print('List after mixing --> ', mixing_list)