def main():

    n = int(input())
    for a in range(n):
        r = input()
        r = r.split(" ")
        for x in range(int(r[0]), int(r[1]) + 1):
            if x > 1:
                for i in range(2, x):
                    if (x % i) == 0:
                        break
                else:
                    print(x)

main()