def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    invs = 0
    for i in range(n - 1):
        if arr[i] == 1 and arr[i + 1] == 0:
            invs += 1
    print(invs + 1)


t = int(input())
for i in range(t):
    solve()