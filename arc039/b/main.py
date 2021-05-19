#!/usr/bin/env python3


def main():
    N, K = map(int, input().split())
    # ans = pow(K // N, N - K % N, m) * pow(K // N + 1, K % N, m)

    p = 10**9+7
    M = 1000
    a = [None] * (M+1)
    inva = [None] * (M+1)
    a[0] = 1

    for i in range(1, M+1):
        a[i] = i * a[i-1] % p

    inva[M] = pow(a[M], p-2, p)
    for i in range(M):
        inva[M-i-1] = inva[M-i] * (M-i) % p

    if N > K:
        ans = (a[N+K-1]*inva[K] % p) * inva[N-1] % p
        print(ans)
    else:
        ans = (a[N]*inva[N-K % N] % p) * inva[K % N] % p
        print(ans)


if __name__ == "__main__":
    main()
