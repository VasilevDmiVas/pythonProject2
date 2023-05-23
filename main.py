# long = input('Введите значение в см' + ' ')
# # b = input('Введите второе число ')
# result = int(long) // 100
# print('Результат = ' + str(result) + ' Метра')
#
# weight = input('Введите значение в кг' + ' ')
# result = int(weight) // 100
# print('Результат = ' + str(result) + ' центнеров')
#
# weight = input('Введите значение в кг' + ' ')
# result = int(weight) // 1000
# print('Результат = ' + str(result) + ' тонн')
#
# day = input('Введите количество дней' + ' ')
# result = (int(day)+234) // 7
# print('Результат = ' + str(result) + ' недель')

# numbers = (252 / 4 + 49 / 7) + 100 / 4
# print()
# print(numbers)

# distance = input('Введите строку ')
# print('Количество символов ' + str(len(distance)))

# distance = input('Введите строку ')
# result = distance.count('в')
# print('Количество символов в = ' + str(result))

# x = int(input('Введите число х:\n')) # 123=132 256=265
# num = x % 10 # 3
# num1 = x % 100 // 10 #2
# num2 = x // 100 # 1 100+20+3
# result = num2 * 100 + num * 10 + num1 * 1
# print(result)

# x = int(input('Введите четырехзначное число х:\n')) # 1234=4321
# num = x // 1000 # 1
# num1 = x // 100 % 10 # 2
# num2 = x % 100 // 10 # 3
# num3 = x % 10 # 4
# result = num3 * 1000 + num2 * 100 + num1 * 10 + num * 1
# print('Результат чтения х спрва на лево ' + str(result))

# x = 5434 # 4543
# y = 7048 # 784
# num = x % 10 #4
# num1 = x // 1000 #5
# num2 = x % 100 // 10 #3
# result_x = num * 1000 + num1 * 100 + num * 10 + num2 * 1
# num3 = y // 1000 #7
# num4 = y % 10 #8
# num5 = y % 48 // 10 #4
# result_y = num3 * 100 +num4 * 10 + num5
# print('Результат x= ' + str(result_x))
# print('Результат y= ' + str(result_y))

# 123 - 321 32
# x = int(input('Введите трехзначное число n от 1 до 999:\n'))
# num = x % 10 #3
# num1 = x // 10 % 10 #2
# num2 = x // 100 #1
# result = num * 100 + num1 * 10 + num2 * 1
# print('Х = ' + str(result))

# a = int(input('Введите число а:\n'))
# b = int(input('Введите число b:\n'))
# if a % b == 0:  # 5 / 2
#     print('Является делителем')
# else:
#     print('Не является делителем')

# a = int(input('Введите 2-х значное число а:\n'))
# if a > 10 and a < 100:
#     num = a % 10
#     if num == 7:
#         print('Введенное число оканчивается на цифру 7 ')
#     else:
#         print('Введенное число не оканчивается на цифру 7 ')
# else:
#     print('Введено не верное число') 52

# a = int(input('Введите 2-х значное число а:\n'))
# if a > 10 and a < 100:
#     num = a % 10
#     num1 = a // 10
#     if num1 > num:
#         print('Введенное 1 число больше 2 ')
#     if num1 < num:
#         print('Введенное 2 число больше 1')
#     else:
#         print('Введенные числа равны')
# else:
#     print('Введено не верное число')

# a = int(input('Введите 2-х значное число а:\n'))
# if a > 10 and a < 100:
#     num = a ** 2
#     num1 = a % 10   # 25 - b
#     num2 = a // 10  # 25 a
#     num3 = 4 * ((num2+num1) * (num2 ** 2 - num2 * num1 + num1 ** 2))
#     if num == num3:
#         print('Равен')
#     else:
#         print('Не равен')
# else:
#     print('Введено не верное число')

# b = int(input('Введите 3-х значное число b: \n'))  #112 = 2 555
# if b > 100 and b < 1000:
#     num = b % 10
#     num1 = b // 10 % 10
#     num2 = b // 100
#     num3 = num * num1 * num2
#     a = int(input('Введите число а:\n'))
#     if num3 < a:
#         print('Число а больше числа b')
#     if num3 == a:
#         print('Число a равно числу b')
# else:
#     print('Введено не верное число')

# print(124%2)
#
#
# m = int(input('Введите число m: \n'))
# if m % 2 == 0:
#     print('Ввели четное число')
    # num = m % 10
    # num1 = m // 10 % 10
    # num2 = m // 100
    # result = num == num1 or num1 == num2
    # if result:
    #     print('Есть одинаковые цифры ')
    # else:
    #     print('Все цифры не одинаковые')
# else:
#     print('Ввели нечетное число')

# a = int(input('Введите число a: \n'))
# b = int(input('Введите число b: \n'))
# c = int(input('Введите число c: \n'))
# if a > b and a > c:
#     print('Число а больше и b и c')
# elif b > a and b > c:
#     print('Число b больше и a и c')
# else:
#     print('Число c больше и a и b')

# a = int(input('Введите число a: \n'))
# b = int(input('Введите число b: \n'))
# if a > b:
#     result = a // 2
#     print('Число а уменьшенное в 2 раза = ' + str(result))
# else:
#     print('Число b больше числа а')

#
# a = int(input('Введите число a: \n'))
# b = int(input('Введите число b: \n'))
# c = int(input('Введите число c: \n'))
# if a % 2 == 0:
#     print('Число а четное и = ' + str(a))
# if b % 2 == 0:
#     print('Число b четное и = ' + str(b))
# if c % 2 == 0:
#     print('Число с четное и = ' + str(c))
# else:
#     print('Ввели нечетные цифры')

# a = int(input('Введите число a: \n'))
# b = int(input('Введите число b: \n'))
# c = int(input('Введите число c: \n'))
# d = int(input('Введите число d: \n'))
#
# if a > 5 and b > 5 and c > 5 and d > 5:
#     result = a + b + c + d
#     print('Сумма чисел a и b и c и d = ' + str(result))
# elif a < 5 and b > 5 and c > 5 and d > 5:
#     result = b + c + d
#     print('Сумма чисел b и c и d  = ' + str(result))
# elif a > 5 and b < 5 and c > 5 and d > 5:
#     result = a + c + d
#     print('Сумма чисел a и c и d = ' + str(result))
# elif a > 5 and b > 5 and c < 5 and d > 5:
#     result = a + b + d
#     print('Сумма чисел a и b и d = ' + str(result))
# elif a > 5 and b > 5 and c > 5 and d < 5:
#     result = a + b + c
#     print('Сумма чисел a и b и c = ' + str(result))
# elif a < 5 and b < 5 and c > 5 and d > 5:
#     result = c + d
#     print('Сумма чисел c и d = ' + str(result))
# elif a > 5 and b > 5 and c < 5 and d < 5:
#     result = a + b
#     print('Сумма чисел a и b = ' + str(result))
# elif a < 5 and b < 5 and c < 5 and d > 5:
#     result = d
#     print('Сумма чисел = ' + str(result))
# else:
#     print('Введенные числа меньше либо равны 5')

# a = int(input('Введите число a: \n'))
# b = int(input('Введите число b: \n'))
# c = int(input('Введите число c: \n'))
# d = int(input('Введите число d: \n'))
#
# if a % 3 == 0 and b % 3 == 0 and c % 3 == 0 and d % 3 == 0: # abcd acd bcd
#     print('Сумма чисел кратных 3 = ' + str(a + b + c + d))
# elif b % 3 == 0 and c % 3 == 0 and d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(b + c + d))
# elif a % 3 == 0 and c % 3 == 0 and d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + c + d))
# elif a % 3 == 0 and b % 3 == 0 and d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + b + d))
# elif a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + b + c))
# elif a % 3 == 0 and b % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + b))
# elif a % 3 == 0 and c % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + c))
# elif a % 3 == 0 and d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a + d))
# elif c % 3 == 0 and d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(c + d))
# elif a % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(a))
# elif b % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(b))
# elif c % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(c))
# elif d % 3 == 0:
#     print('Сумма чисел кратных 3 = ' + str(d))
# else:
#     print('Введенных чисел кратных 3 нет')

# a = int(input('Введите число a: \n'))
# if a == 1:
#     print ('Понедельник')
# elif a == 2:
#     print ('Вторник')
# elif a == 3:
#     print ('Среда')
# elif a == 4:
#     print('Четверг')
# elif a == 5:
#     print('Пятница')
# elif a == 6:
#     print('Суббота')
# elif a == 7:
#     print('Воскресенье')
# else:
#     print('Error')
# Цикл с условием

# countNumber = 0
# summ = 0
# while countNumber < 3: # Пока количество введенных символов < 3
#     number = int(input('Введите число \n'))
#     summ = summ + number
#     countNumber = countNumber + 1
# print('Сумма =', summ)

# summ = 0
# while summ < 20: # Пока сумма < 20
#     print('Сумма -', summ)
#     number = int(input('Введите число \n'))
#     summ = summ + number
# print('Сумма =', summ)

# countNumber = 0
# pr = 1
# while countNumber < 5:
#     number = int(input('Введите число \n'))
#     pr = number * pr
#     countNumber = countNumber + 1
# print('Произведение =', pr)

# number = int(input('Введите число\n'))
# cnt = 0
# while number > 0:
#     num = number % 10 # переход в конец введенного числа
#     if num == 3:
#         cnt = cnt + 1
#     number = number // 10 # отделение последнего числа
# print('Количество 3 в введенном числе =', cnt) 125693

# number = int(input('Введите число\n'))
# maks = 0
# while number > 0:
#     num = number % 10 # переход в конец введенного числа
#     if num > maks:
#         maks = num
#     number = number // 10 # отделение последнего числа
# print('Максимальное число =', maks)

# ДЗ 6.8 пока квадрат числа не станет больше n вводится с клавы
# 6.22 г, д
# 6.23 а, в
# 6.27 б

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
