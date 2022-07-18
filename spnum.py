import sys

input = sys.stdin.readline

MAXN = 10000000


def sumOfDigits(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum


def solve(n):
    res = -1
    for i in range(n, MAXN):
        s = sumOfDigits(i)
        if s % 4 == 0:
            return i
    return -1


for _ in range(int(input())):
    print(solve(int(input())))