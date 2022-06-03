'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
'''
spisok = [1,5,4,6,9]
sum = 0
for i in range(0,len(spisok)):
    if i%2 == 0:
        sum = sum + spisok[i]
print(sum)
'''

'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

spisok_1 = [1,5,6,4,1]
f = 0
itog = []
if len(spisok_1) % 2 == 1:
 a = (round(len(spisok_1)/2))+1
else:
 a = len(spisok_1) / 2
for i in range(0,a):
    f = spisok_1[i] * spisok_1[len(spisok_1)-(i+1)]
    itog.append(f)
print(itog)


Задайте список из вещественных чисел. Напишите программу, которая 
найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19



spisok_2 = [1.2, 5.9, 6.6, 4.011, 1.75]
spisok_3 = []
for i in spisok_2:
    spisok_3.append(i%1)
print(max(spisok_3)-(min(spisok_3)))


Напишите программу, которая будет преобразовывать десятичное число в двоичное.


chislo = 12
result = " "
while chislo > 0:
    result = str(chislo % 2) + result
    chislo = chislo//2
print(result)

Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

'''
print ('Введите число: ')
f = int (input())
i = 0
a = 0
b = 1

sum = 0
fib_spisok = [a, b]
while i<(f-1):
    sum = a+b
    fib_spisok.append(sum)
    a = b
    b = sum
    i = i + 1
#print (fib_spisok)

a = 1
b = -1
i=0
fib_otric = [b,a]
while i<abs(f-2):
    znach = a - b
    fib_otric.insert(0, znach)
    a = b
    b = znach
    i = i + 1
print(fib_otric+fib_spisok)


