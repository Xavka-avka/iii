a = []
n = int(input("Введите количество элементов: "))
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
for i in s[::2]:
    if i % 2 == 0:
        print(i, end=" ")

