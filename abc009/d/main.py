#!/usr/bin/env python3
from copy import deepcopy


def main():
    K, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    if M <= K:
        print(A[M-1])
        exit()
    now = [[0] * K for _ in range(K)]
    for i in range(K):
        now[i][i] = (1 << 32)-1
    mul = [[0] * K for _ in range(K)]
    mul[0] = C[:]
    for i in range(K - 1):
        mul[i + 1][i] = (1 << 32) - 1

    N = M-K  # 行列累乗
    while N > 0:
        if N % 2 > 0:
            # now *= mul
            tmp = [[0] * K for _ in range(K)]
            for i in range(K):
                for j in range(K):
                    res = 0
                    for k in range(K):
                        res ^= (now[i][k] & mul[k][j])
                    tmp[i][j] = res
            now = deepcopy(tmp)
        # mul * mul
        tmp = [[0] * K for _ in range(K)]
        for i in range(K):
            for j in range(K):
                res = 0
                for k in range(K):
                    res ^= (mul[i][k] & mul[k][j])
                tmp[i][j] = res
        mul = deepcopy(tmp)
        N //= 2
    ans = 0
    for k in range(K):
        ans ^= (now[0][k] & A[K-k-1])
    print(ans)


if __name__ == "__main__":
    main()
