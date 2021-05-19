#!/usr/bin/env python3


def main():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))
    R.sort()
    ans = 0
    for i in range(K):
        ans = (ans + R[N-K:][i])/2
    print(ans)

if __name__ == "__main__":
    main()
