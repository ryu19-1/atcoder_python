#!/usr/bin/env python3


def main():
    N = int(input())
    F = [None for _ in range(N)]
    for i in range(N):
        F[i] = list(map(int, input().split()))
    
    P = [None for _ in range(N)]
    for i in range(N):
        P[i] = list(map(int, input().split()))

    ans = -10**10

    for i in range(1,2**10):
        c = [0] * N
        for j in range(10):
            if (i >> j) & 1:
                for k in range(N):
                    c[k] += F[k][j]
        
        tmp = 0
        for k in range(N):
            tmp += P[k][c[k]]
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
