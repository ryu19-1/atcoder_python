#!/usr/bin/env python3
from itertools import accumulate

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(accumulate([0] + a))
    ans = 0
    for i in range(N-K+1):
        ans += a[i+K] - a[i]
    print(ans)


if __name__ == "__main__":
    main()
