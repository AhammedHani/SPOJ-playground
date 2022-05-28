for x in range(int(input())):
    n1, n2 = input(), input()
    print(int(str(int(str(n1)[::-1]) + int(str(n2)[::-1]))[::-1]))
