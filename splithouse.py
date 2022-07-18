class houses:
    def house(self, n, pattern):
        while n != 0:
            if pattern.find('HH') != -1:
                return 'NO'
            else:
                pattern = pattern.replace('.', 'B')
                return (f"YES\n{pattern}")


def main():
    n = int(input())
    pattern = input()
    op = houses()
    ans = op.house(n, pattern)
    print(ans)


if __name__ == '__main__':
    main()