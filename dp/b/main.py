#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    INF = 10**12
    dp = [INF] * N
    dp[0] = 0
    for i in range(1,N):
        dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,min(K,i)+1))
    print(dp[N-1])

if __name__ == "__main__":
    main()