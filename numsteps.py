ip = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
f = 0
i = 0
mi = min(a)
while i < ip and mi > -1:
    if a[i] > mi and (a[i] - mi) >= b[i]:
        n = (a[i] - mi) // b[i]
        c += n
        a[i] = a[i] - (b[i] * n)
    elif a[i] > mi and a[i] >= a[i] - b[i]:
        c += 1
        a[i] = a[i] - b[i]
    if a[i] < mi:
        mi = a[i]
        i = -1
    i += 1
if min(a) < 0:
    print(-1)
else:
    print(c)