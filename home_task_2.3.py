# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#   Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}}  ?????

#           {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
#           14.071722992112484

number_n = int(input('Enter the number "n" to create a sequence: '))

sequence_number = {}
for i in range(1, number_n + 1):
    sequence_number[i] = (1 + 1 / i) ** i
print('List of sequence elements', sequence_number)

summ = 0
for i in sequence_number:
    summ += float(sequence_number[i])
print('Sum of sequence elements', summ)