from math import sqrt


def task2():
    b = 999
    print("Вводите числа:")
    while True:
        while True:
            c = int(input())
            if c < 1000:
                if c < b and c != 999:
                    b = c
                    continue
                elif c == 999:
                    print(f"Наименьшее из введённых чисел: {b}")
                    return
            else:
                print("Вводите целые числа, которые меньше 1000")


def task3():
    n = int(input("Сколько чисел вы хотите ввести?\n"))
    t = int(input())
    g = 1
    if t < 1:
        print("Пишите только неотрицательные числа!")
        return
    if n == 1:
        print(sqrt(t))
        return
    for i in range(n-1):
        b = int(input())
        if b < 1:
            print("Пишите только неотрицательные числа!")
            return
        if b < t:
            t = b
        if g == n - 1:
            print(f"Наименьшее введённое число: {t}")
            print(f"Корень этого числа: {sqrt(t)}")
            return
        g += 1


def task4():
    summ = int(input("Введите денежную сумму: "))
    for i in range(4):
        if i >= 1:
            n = 10 ** (3 - i)
        else:
            n = 500
        cnt = summ // n
        summ -= cnt * n
        if cnt > 0:
            print(f'{cnt} по {n} {"рублей" if n != 1 else "рублю"}')
    return


def task5():
    min_number = int(input("Вводите числа:\n"))
    while True:
        i = input()
        if i == ".":
            break
        i = int(i)
        if 0 < i < min_number:
            min_number = i
    print(f"Минимальное целое положительное введённое число: {min_number}")
    return


print("Какую задачу вы хотите запустить?(напишите число от 2 до 5)")
a = int(input())
if a == 2:
    print("2 Задача:")
    task2()
if a == 3:
    print("3 Задача:")
    task3()
if a == 4:
    print("4 Задача:")
    task4()
if a == 5:
    print("5 Задача:")
    task5()
