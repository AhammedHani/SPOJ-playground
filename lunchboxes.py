schools = int(input())
for i in range(schools):
    list1 = list(map(int , input().split()))
    list2 = list(map(int , input().split()))
    n = list1[0]
    k = list1[1]
    count = 0
    sums = 0
    list2.sort()
    for i in list2:
        sums = sums + i
        if sums>n:
            print(count)
            break
        else:
            count = count + 1
    else:
        if sums <= n:
            print(k)