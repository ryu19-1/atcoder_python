while (True):
    n, w, d = map(int, input().split())
    if n == w == d == 0:
        break
    pieces = []
    pieces.append([0, 0, w, d])
    for i in range(n):
        p, s = map(int, input().split())
        p -= 1
        a, b, c, d = pieces.pop(p)
        s %= 2*(c+d-a-b)
        if s < (c - a):
            if 2*s < c-a:
                pieces.append([a, b, a + s, d])
                pieces.append([a+s, b, c, d])
            else:
                pieces.append([a+s, b, c, d])
                pieces.append([a, b, a + s, d])
        elif s < (c + d - a - b):
            s -= (c - a)
            if 2*s < d-b:
                pieces.append([a, b, c, b+s])
                pieces.append([a, b + s, c, d])
            else:
                pieces.append([a, b + s, c, d])
                pieces.append([a, b, c, b+s])
        elif s < (d - b + 2*(c - a)):
            s -= (c + d - a - b)
            if 2*s < c-a:
                pieces.append([c-s, b, c, d])
                pieces.append([a, b, c - s, d])
            else:
                pieces.append([a, b, c - s, d])
                pieces.append([c-s, b, c, d])
        else:
            s -= (d - b + 2 * (c - a))
            if 2*s < d-b:
                pieces.append([a, d-s, c, d])
                pieces.append([a, b, c, d - s])
            else:
                pieces.append([a, b, c, d - s])
                pieces.append([a, d-s, c, d])
        # pieces.sort()
    [print((p[3]-p[1])*(p[2]-p[0])) for p in pieces]
