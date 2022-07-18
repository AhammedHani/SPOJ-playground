def minUpdates(N, A, K):
    if N % 2 != 0:
        return -1

    sA = set(A)
    num_to_replace = len(A) - len(sA)

    num_even = 0
    num_even_available = K // 2
    num_odd_available = K - num_even_available
    for a in sA:
        if a <= K:
            if a % 2 == 0:
                num_even += 1
                num_even_available -= 1
            else:
                num_odd_available -= 1
        else:
            if a % 2 == 0:
                num_even += 1

    good_even = N // 2
    num_even_to_add = num_odd_to_add = 0

    if good_even < num_even:
        num_to_replace += num_even - good_even
        num_odd_to_add = num_to_replace
    else:
        if num_to_replace < (good_even - num_even):
            num_to_replace = good_even - num_even
            num_even_to_add = num_to_replace
        else:
            num_even_to_add = good_even - num_even
            num_odd_to_add = num_to_replace - num_even_to_add

    if num_even_available < num_even_to_add:
        return -1
    if num_odd_available < num_odd_to_add:
        return -1
    return num_to_replace


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = minUpdates(N, A, K)
    print(out_)