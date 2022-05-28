def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(int(input())):
    n = int(input())
    print(factorial(n))
