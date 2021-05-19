#!/usr/bin/env python3


def main():
    T = int(input())
    m = 10**9+7
    for _ in range(T):
        N, A, B = map(int, input().split())
        if A + B > N:
            print(0)
            continue
        res = (N - A + 1) * (N - B + 1) % m
        t = (N - A - B + 2) * (N - A - B + 1) // 2
        t %= m
        res = res * t % m
        res = res * 4 % m
        tmp = pow(t, 2, m) * 4 % m
        res -= tmp
        print(res % m)


if __name__ == "__main__":
    main()
