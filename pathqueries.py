from sys import stdin, stdout


def main():
    read = stdin.readline
    write = stdout.write
    t = int(read())
    for t_ in range(t):
        n, q = map(int, read().split())
        a = [0] + list(map(lambda x: int(x) & 1, read().split()))
        # we do not need edges, but have to read them
        for n_ in range(n - 1): read()
        o = sum(a)
        e = n - o
        out = []
        for q_ in range(q):
            u, val = map(int, read().split())
            val &= 1
            if a[u] and not val:
                o -= 1; e += 1; a[u] = val
            elif not a[u] and val:
                o += 1; e -= 1; a[u] = val
            out.append(str(o * (o + 1) // 2 + e * (e + 1) // 2))
        write(" ".join(out) + '\n')


if __name__ == "__main__": main()