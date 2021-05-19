#!/usr/bin/env python3


def main():
    # 方針: 足してxになるy個の整数の組み合わせの数を前計算する
    # 1<= x <= N, 1<= y <= K*N
    N, K, M = map(int, input().split())
    NN = N * (N+1)//2
    dp = [[0] * (K * NN + 1) for _ in range(K * N + 1)]
    dp[0][0] = 1
    lim = K*NN

    for i in range(1, N+1):
        for y in range(K*N-1, -1, -1):
            for x in range(K * NN + 1):
                if dp[y][x] == 0:
                    continue
                for k in range(1, K + 1):
                    t = i*k
                    if y + k > K * N:
                        break
                    if x + t > lim:
                        break
                    dp[y + k][x + t] += dp[y][x]
                    dp[y + k][x + t] %= M

    for i in range(1, N + 1):
        ans = 0
        for j in range(1, K * N + 1):
            if i * j > NN*K:
                break
            ans += dp[j][i*j]
            ans %= M
        print(ans)


if __name__ == "__main__":
    main()
