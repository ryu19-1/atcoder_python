#!/usr/bin/env python3


def main():
    N = int(input())
    Q = int(input())
    r = list(range(N))# 行番号 + 列番号
    c = list(range(N))# 行番号 + 列番号
    flag = 0
    for _ in range(Q):
        q = list(map(lambda x: int(x)-1, input().split()))
        if q[0] == 1:
            c[q[1]],c[q[2]] = c[q[2]],c[q[1]]
        elif q[0] == 0:
            r[q[1]],r[q[2]] = r[q[2]],r[q[1]]
        elif q[0] == 2:
            flag += 1
            r,c = c,r
        else:
            i = r[q[1]]
            j = c[q[2]]
            if flag % 2 == 1:
                print(N*j+i)
            else:
                print(N*i+j)

if __name__ == "__main__":
    main()
