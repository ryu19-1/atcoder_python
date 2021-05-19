#!/usr/bin/env python3

def main():
    D, N = map(int, input().split())
    T = [int(input()) for _ in range(D)]
    ok = [[0] * N for _ in range(D)]
    C = [None] * N

    for i in range(N):
        a, b, C[i] = map(int, input().split())
        for j in range(D):
            if a <= T[j] <= b:
                ok[j][i] = 1# この服をこの日に着ても良い

    dp = [[0] * N for _ in range(D+1)]

    for i in range(1,D):
        for j in range(N):
            if ok[i][j]:
                tmp = 0
                for k in range(N):
                    if ok[i-1][k]:
                        tmp = max(tmp, dp[i-1][k]+ abs(C[k]-C[j]))
                dp[i][j] = tmp

    print(max(dp[D-1]))

if __name__ == "__main__":
    main()
