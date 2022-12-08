A = int(input())
previous = 0
previous2 = 1
n = 2
if A == 0:
    print("1")
    exit()
elif A == 1:
    print("2 and 3")
    exit()
elif A < 0:
    print("-1")
    exit()

while True:
    if A == previous + previous2:
        print(n)
        break
    elif previous2 < A < previous:
        print("-1")
        break
    previous, previous2, = previous + previous2, previous
    n += 1
