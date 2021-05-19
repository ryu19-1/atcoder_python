#!/usr/bin/env python3


def op1():
    return [
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1]
    ]


def op2():
    return [
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ]


def op3(p):
    return [
        [-1, 0, 2*p],
        [0, 1, 0],
        [0, 0, 1]
    ]


def op4(p):
    return [
        [1, 0, 0],
        [0, -1, 2*p],
        [0, 0, 1]
    ]


def dot(a, b):
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0],
         a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1],
         a[0][0]*b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0],
         a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1],
         a[1][0]*b[0][2] + a[1][1]*b[1][2] + a[1][2]*b[2][2]],
        [a[2][0]*b[0][0] + a[2][1]*b[1][0] + a[2][2]*b[2][0],
         a[2][0]*b[0][1] + a[2][1]*b[1][1] + a[2][2]*b[2][1],
         a[2][0]*b[0][2] + a[2][1]*b[1][2] + a[2][2]*b[2][2]]
    ]


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    ops = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    adj = [[] for _ in range(M+1)]
    for i in range(Q):
        A, B = map(int, input().split())
        adj[A].append((B-1, i))

    ans = [None] * Q
    nowop = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for i in range(M + 1):
        p = 0
        if i > 0:
            # 関数合成する
            if ops[i - 1][0] == 1:
                matrix = op1()
            elif ops[i - 1][0] == 2:
                matrix = op2()
            elif ops[i - 1][0] == 3:
                p = ops[i - 1][1]
                matrix = op3(p)
            else:
                p = ops[i - 1][1]
                matrix = op4(p)
            nowop = dot(matrix, nowop)
        for B, i in adj[i]:
            x = XY[B][0]
            y = XY[B][1]
            ans[i] = [nowop[0][0]*x+nowop[0][1]*y+nowop[0][2],
                      nowop[1][0]*x+nowop[1][1]*y+nowop[1][2]]
        # print(i, nowop)

    for i in range(Q):
        print(ans[i][0], ans[i][1])


if __name__ == "__main__":
    main()
