#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    A = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        A[a] = b
    
    dp = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(N+1)]

    d123 = []
    for i in range(1,4):
        if A[i] == 0:
            d123.append([0,1,2])
        else:
            d123.append([A[i]-1])

    for j in d123[0]:
        for k in d123[1]:
            for l in d123[2]:
                dp[3][j][k][l] = 1

    for i in range(4,N+1):
        if A[i] == 0:
            now = [0,1,2]
        else:
            now = [A[i]-1]

        for l in now:
            for j in range(3):
                for k in range(3):
                    if j == k == l: continue
                    for h in range(3):
                        if h == j == k: continue
                        dp[i][j][k][l] += dp[i-1][h][j][k]

    ans = 0
    for j in range(3):
        for k in range(3):
            for l in range(3):
                # if dp[N][j][k][l]:
                    # print(j,k,l)
                ans += dp[N][j][k][l]
                ans %= 10000
    print(ans)
    # print(dp[N])

if __name__ == "__main__":
    main()
