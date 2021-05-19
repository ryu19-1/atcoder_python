#!/usr/bin/env python3


def main():
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    indices = [[-1, N] for _ in range(C)]
    for i in range(N):
        indices[a[i] - 1].append(i)

    ans = 0
    pattern = N*(N+1)//2
    for i in range(C):
        res = pattern
        indices[i].sort()
        for j in range(len(indices[i]) - 1):
            tmp = indices[i][j + 1] - indices[i][j]-1
            res -= tmp * (tmp + 1) // 2
        print(res)


if __name__ == "__main__":
    main()
