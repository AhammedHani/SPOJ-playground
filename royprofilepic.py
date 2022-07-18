def p(l, w, h):
    if w < l or h < l:
        return 'UPLOAD ANOTHER'
    if w == h:
        return 'ACCEPTED'
    else:
        return 'CROP IT'


l = int(input())
n = int(input())
for _ in range(n):
    w, h = map(int, input().split())
    print(p(l, w, h))
