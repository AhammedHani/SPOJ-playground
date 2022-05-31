n = int(input())
for x in range(n):
    n1 = int(input())
    n2 = int(input())
    n3 = n1 + n2
    print(" ", n1)
    print("+", n2)
    print("-" * len(str(n3)))
    print(" ", n3)

    n1 = int(input())
    n2 = int(input())
    n3 = n1 - n2
    print(" ", n1)
    print("-", n2)
    print("-" * 6)
    print(" ", n3)

    n1 = int(input())
    n2 = int(input())
    n3 = n1 * n2
    print(" ", n1)
    print("*", n2)
    print("-" * 6)
    print(" ", n3)

    n1 = int(input())
    n2 = int(input())
    n3 = n1 / n2
    print(" ", n1)
    print("/", n2)
    print("-" * 6)
    print(" ", n3)
