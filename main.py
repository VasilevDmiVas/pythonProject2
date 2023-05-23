# 6.22 г
# number = int(input('Введите число\n'))
# suma = 0
# while number > 0:
#     num = number % 10 # переход в конец введенного числа
#     if num > 5:
#         suma = suma + num
#     number = number // 10 # отделение последнего числа
# print('Сумма чисел больше 5 =', suma)

# 6.22 д
# number = int(input('Введите число\n'))
# proizved = 1
# while number > 0:
#     num = number % 10 # переход в конец введенного числа
#     if num > 7:
#         proizved = proizved * num
#     number = number // 10 # отделение последнего числа
# print('Произведение чисел больше 7 =', proizved)

# 6.23 a
# number = int(input('Введите число\n'))
# number1 = int(input('Введите число\n'))
# CountNumber = 0
# while number > 0:
#     num = number % 10
#     if number1 == num:
#         CountNumber = CountNumber + 1
#     number = number // 10
# print(number1, 'встретилась ',CountNumber, 'раз')

# 6.23 в
# number = int(input('Введите число\n'))
# number1 = int(input('Введите число a:\n'))
# CountNumber = 0
# while number > 0:
#     num = number % 10
#     if number1 and num >= 9:
#         CountNumber = CountNumber + num
#     number = number // 10
# print('Сумма = ', CountNumber)

# 6.27 б

# number = int(input('Введите число\n'))
# maxNumber = 0
# minNumber = 0
# while number > 0:
#     num = number % 10 # переход в конец введенного числа
#     if num > maxNumber:
#         maxNumber = num
#     else:
#         minNumber = num
#     number = number // 10 # отделение последнего числа
# c = maxNumber - minNumber
# # print('Максимальное число =', maxNumber)
# # print('Минимальное число =', minNumber)
# print('На', c, 'максимальное превышает минимальное')

# 6.10 a
# number = int(input('Введите число\n'))
# num = 0
# while num ** 2 < number:
#     num = num + 1
#     print(num)
