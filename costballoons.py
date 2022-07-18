for i in range(int(input())):
    n1, n2 = map(int, input().split())
    m = int(input())
    l1 = []
    l2 = []
    ans = 0
    for i in range(m):
        m1, m2 = map(int, input().split())
        l1.append(m1)
        l2.append(m2)
    if l1.count(1) > l2.count(1):
        ans = (l1.count(1)) * min(n1, n2)
        ans = ans + l2.count(1) * max(n1, n2)
    else:
        ans = (l2.count(1)) * min(n1, n2)
        ans = ans + l1.count(1) * max(n1, n2)
    print(ans)