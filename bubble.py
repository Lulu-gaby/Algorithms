mas = [10, 3, 6, 4, 7, 2, 8, 1]
n = 8
for run in range(n - 1):
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)