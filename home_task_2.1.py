# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#   6782 -> 23
#   0,56 -> 11

def natural(number: int):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
    return summ


def material(a: int, b: int):
    summ = 0
    while a != 0:
        summ += a % 10
        a = a // 10
    while b != 0:
        summ += b % 10
        b = b // 10
    return summ


number = input("Enter a positive number: ")
point = number.find('.')

if point == -1:
    number = int(number)
    if number < 0:
        number *= -1
    print(f'The sum of digits of a natural integer {number} is equal to: ', natural(number))

else:
    x = number.split('.')
    a = int(x[0])
    b = int(x[1])
    print(f'The sum of the digits of a real number {number} is equal to: ', material(a, b))
