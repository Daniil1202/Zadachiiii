# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# num = input('Введите 3-х значное число: ')
# res = 0
# if len(num) == 3:
#     for i in num:
#         res += int(i)
#     print(res)
# else:
#     print('Вы ввели не 3-х значное число')




# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
#  сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10



# s = 24
# print('Петя и Сережа сделали по', s/6, 'шт')
# print('Маша сделала ', s/6*4, 'шт')




# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# t = input ('ВВедите номер билета : ')
# i = int (t[0])+ int (t[1]) + int (t[2])
# r = int (t[3]) + int (t[4]) + int (t[5])
# if i ==r:
#     print ('yes') 
# else :
#     print('no')



#     Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


# n,m,k = int(input('1-я сторона : ')), int(input('2-я сторона: ')), int (input('количество долек: '))
# if k%n == 0 or k%m == 0 :
#     print('Yes')
# else : print('No')