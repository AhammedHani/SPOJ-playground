for x in range(int(input())):
    n = int(input())
    count = 0
    if n >= 5:
        while n >= 5:
            n = n // 5
            count = count + n
        print(count)
    else:
        print(0)
