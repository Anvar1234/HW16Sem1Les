# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input("Введите 3-х значное число: "))
# sumOfDigit = 0
# while number > 0:
#     sumOfDigit += number % 10
#     number = number // 10
# print(sumOfDigit)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# sum = int(input("Сколько всего журавлей сделали детишки: "))

# sergAndPetya = int(sum / 6)
# katya = sergAndPetya * 4
# petya = sergAndPetya
# serg = sergAndPetya

# print(petya, katya, serg)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

# #Вариант 1. Математический.

# number = int(input("Введите число из билета: "))
# if number//100000 < 1 or number//100000 > 6:
#     print("Введено некорректное число")
#     quit()
# firstNumber = 0
# secondNumber = 0
# for i in range(3):
#     firstNumber += number % 10
#     number //= 10
# #print(firstNumber)
# for i in range(3):
#     secondNumber += number % 10
#     number //= 10
# #print(secondNumber)
# if firstNumber == secondNumber:
#     print("yes")
# else:
#     print("no")


#Вариант 2. Строковый (работает корректно, даже если номер начинается с 0)

# number = input("Введите число из билета: ")

# if len(number) < 6 or len(number) > 6:
#     print("Введено некорректное число")
#     quit()
# firstSum = 0
# secondSum = 0
# for i in range(3):
#     firstSum += int(number[i])
# #print(firstSum)
# for i in range(3,6):
#     secondSum += int(number[i])
# #print(secondSum)

# if firstSum == secondSum:
#     print("yes")
# else:
#     print("no")