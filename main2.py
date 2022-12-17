"""c = open('class.txt', 'r', encoding='utf-8')
fc = c.read().split("\n")

summ = 0
for item in fc:
    mark = int(item.split()[2])
    if mark < 3:
        print(item)
    summ += mark

print(round(summ/len(fc), 2))"""

c = open('class.txt', 'r', encoding='utf-8')
strings = c.readlines()
print(f'Количество строк в файле: {len(strings)}')
n_string = 1
for item in strings:
    print('='*8 + f' Линия {n_string} ' + '='*8)
    print(f'Слов в строке {n_string}: {item.count(" ") + 1}')
    print(f'Символов в строке {n_string}: {len(item.strip())}')
    n_string += 1
