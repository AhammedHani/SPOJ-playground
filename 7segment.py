t = int(input())
l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for _ in range(t):
    n = input()
    y = 0
    for i in n:
        y = y + l[int(i)]

    if y % 2 == 0:
        y = y / 2
        print('1' * int(y))
    else:
        y = (y - 1) / 2
        s = str('1' * int(y - 1))
        print('7' + s)