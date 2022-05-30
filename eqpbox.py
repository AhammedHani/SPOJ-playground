for x in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a > c or b > d:
        print("Escape is possible")
    else:
        print("Box cannot be dropped")
