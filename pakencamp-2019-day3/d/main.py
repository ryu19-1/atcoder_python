#!/usr/bin/env python3

def main():
    N = int(input())
    S = [input() for _ in range(5)]
    INF = 1e12

    dp = [[INF]*3 for _ in range(N+1)]
    dp[0] = [0, 0, 0]

    for i in range(1,N+1):
        count = [0, 0, 0]
        for h in range(5):
            if S[h][i-1] in 'RBW':
                count['RBW'.index(S[h][i-1])] += 1
        for j in range(3):
            for k in range(3):
                if j == k: continue
                dp[i][j] = min(dp[i][j], dp[i-1][k]+(5-count[j]))
    
    print(min(dp[N]))

if __name__ == "__main__":
    main()
