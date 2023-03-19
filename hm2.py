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