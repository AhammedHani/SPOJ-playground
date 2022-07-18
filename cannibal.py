def Minimum_Operations(n, s):
    nr_operations = 0
    counter = {i: s.count(i) for i in set(s)}
    out = 0
    for char, freq in counter.items():
        if freq == 2: out += 1
        if freq > 2: out += (freq // 2)
    return out


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()

    out_ = Minimum_Operations(n, s)
    print(out_)