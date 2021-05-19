#!/usr/bin/env python3

from itertools import accumulate


def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + [*accumulate(a)]
    candidate = []
    for i in range(N):
        for j in range(i, N):
            candidate.append(a[j + 1] - a[i])

    L = 40
    for i in range(L-1, -1, -1):
        cnt = 0
        next_candidate = []
        for c in candidate:
            if (c >> i) & 1:
                cnt += 1
                next_candidate.append(c)
        if cnt >= K:
            candidate = next_candidate[:]
    ans = (1 << L) - 1
    for c in candidate:
        ans &= c
    print(ans)


if __name__ == "__main__":
    main()
