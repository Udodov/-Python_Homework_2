# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

def sequence(n: int):
    list_elements = [i for i in range(-n, n + 1)]
    return list_elements


def multi_positions(positions: list):
    result = 1
    print('\nValues of selected positions:', end=' ')
    for i in range(len(positions)):
        print(f'{sequence(n)[positions[i]]}', end=' ')
        result *= sequence(n)[positions[i]]
    return result


n = int(input('Enter the number "n" to create a list of items: '))
positions = list(map(int, input('Enter the desired item positions separated by a space --> ').split()))

print('\nYour list:', sequence(n))
print('\nThe product of these positions =', multi_positions(positions))

# def sequence(n: int):
#     list_elements = [-n]
#     for i in range(1, 2 * n + 1):
#         list_elements.append(list_elements[i - 1] + 1)
#     return list_elements


# n = int(input('Enter the number "n" to create a sequence: '))
# print(sequence(n))