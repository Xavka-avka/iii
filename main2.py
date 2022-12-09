n = int(input())
if n > 0:
    for i in range(1, n+1):
        if 5 <= i <= 9:
            continue
        elif 17 <= i <= 37:
            continue
        elif 78 <= i <= 87:
            continue
        else:
            print(i)
else:
    print("Введите натуральное число!")
