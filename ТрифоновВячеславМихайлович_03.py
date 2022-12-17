def task2():
    str_1 = input("Введите строку: ")
    print(str_1[1])
    print(str_1[-2])
    print(str_1[:3])
    print(str_1[:-2])
    print(str_1[::-2])
    print(len(str_1))
    return


def task3():
    stroka = input("Введите строку: ")
    simvol = input("Введите символ, который хотите найти: ")
    print(f"Таких символов {stroka.count(simvol)}")
    return


def task4():
    korteg = (13, 2, 23, 14, 5)
    print(f"Элементы кортежа {korteg}, больше 10: ")
    for i in range(len(korteg)):
        print(korteg[i], end=" ") if korteg[i] > 10 else True
    print("")
    return


def task5():
    str_1 = input("Введите строку: ")
    if "5" not in str_1:
        print("В строке нет цифры 5")
        return
    count = 0
    for i in str_1:
        if i == '5':
            count += 1
    print(count)
    if count == 1:
        print("Индекс цифры 5: ", str_1.find("5"))
        return
    elif count == 2:
        print(f"Индекс первой цифры 5: {str_1.find('5')}, индекс последней цифры 5: {str_1.rfind('5')}")
        return
    else:
        print(f"Индекс первой цифры 5: {str_1.find('5')}, "
              f"индекс второй цифры 5: {str_1.find('5', str_1.find('5') + 1, str_1.rfind('5'))}, "
              f"индекс последней цифры 5: {str_1.rfind('5')}")
        return


def task6():
    student1 = "Иванов Иван Иванович 8а"
    student2 = "Петров Петр Петрович 10б"
    student3 = "Ашин Антон Михайлович 9э"
    student1, student2, student3 = student1.split(), student2.split(), student3.split()
    print(f"|{'Фамилия':<13}|{'Имя':<13}|{'Отчество':>13}|{'Класс':^13}|")
    print(f"|{student1[0]:<13}|{student1[1]:<13}|{student1[2]:>13}|{student1[3]:^13}|")
    print(f"|{student2[0]:<13}|{student2[1]:<13}|{student2[2]:>13}|{student2[3]:^13}|")
    print(f"|{student3[0]:<13}|{student3[1]:<13}|{student3[2]:>13}|{student3[3]:^13}|")
    return


while True:
    a = input("Какую задачу вы хотите запустить?(введите число от 2 до 6): ")
    try:
        a = int(a)
        if a == 2:
            print("2 Задача:")
            task2()
        elif a == 3:
            print("3 Задача:")
            task3()
        elif a == 4:
            print("4 Задача:")
            task4()
        elif a == 5:
            print("5 Задача:")
            task5()
        elif a == 6:
            print("6 Задача:")
            task6()
        else:
            print("Введите только номер нужной задачи!")
    except ValueError:
        print("Введите верный НОМЕР задачи!")
