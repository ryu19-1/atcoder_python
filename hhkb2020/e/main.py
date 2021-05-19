#!/usr/bin/env python3
import sys
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    K = 0
    m = 10**9 + 7

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                K += 1
    ans = K * pow(2, K, m) % m

    dp = [[0]*(H*W) for _ in range(4)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for dy, dx, k in [(-1, 0, 1), (0, -1, 3)]:
                y = i + dy
                x = j + dx
                if 0 <= y < H and 0 <= x < W and S[y][x] == '.':
                    dp[k][W * i + j] = dp[k][W * y + x] + 1

    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if S[i][j] == '#':
                continue
            for dy, dx, k in [(1, 0, 0), (0, 1, 2)]:
                y = i + dy
                x = j + dx
                if 0 <= y < H and 0 <= x < W and S[y][x] == '.':
                    dp[k][W * i + j] = dp[k][W * y + x] + 1
    # print(dp)
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            tmp = 1
            for k in range(4):
                tmp += dp[k][W*i+j]
            ans -= pow(2, K - tmp, m)
    print(ans % m)


if __name__ == "__main__":
    main()
