Урок 2. Циклы (for, while)
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые нужно перевернуть

Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.






#1
n_coins = int(input("Введите количество монеток: "))
eagle_coin = 0
tale_coin = 0
for i in range(n_coins):
    if n_coins >= 0:
        eagle_coin += 1
    else:
        tale_coin += 1
if eagle_coin > tale_coin:
    print(tale_coin)
else:
    print(eagle_coin)

#2

student_x = int(input())
student_y = int(input())
for i in range(student_x):
    for j in range(student_y):
        if student_x == i + j and student_y == i * j:
            print(i, j)

#3
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

