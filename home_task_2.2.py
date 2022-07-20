# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#   Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def set_product_numbers(number_N: int):
    multiplier = [1]
    for i in range(1, number_N):
        multiplier.append(multiplier[i - 1] * (i + 1))
    return multiplier


number_N = int(input('Enter the number "N" to create a multiplication set: '))
if number_N < 0:
    number_N *= -1
print(f'Multiplication of numbers, from 1 to a number '
      f'{number_N} looks like this:', set_product_numbers(number_N))
