for x in range(int(input())):
    a = []
    sp = []
    for i in input():
        if i.isalpha():
            a.append(i)
        elif i == ')':
            a.append(sp.pop())
        elif i == '(':
            pass
        else:
            sp.append(i)
    print("".join(a))
