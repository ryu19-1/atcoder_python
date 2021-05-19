#!/usr/bin/env python3
from bisect import bisect_left
from itertools import accumulate


def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    # i0 = bisect_left(x,0)
    # pos = list(accumulate(x[i0:]))
    # neg = list(accumulate(x[:i0][::-1]))
    # y = neg[::-1] + pos
    ans = 10**18
    for i in range(N-K+1):
        # x[i] と x[i+K-1]の符号が違う
        p, q = abs(x[i]), abs(x[i+K-1])
        if x[i] * x[i+K-1] < 0:
            ans = min(ans, p + q + min(p,q) )
        else:
            ans = min(ans, max(p,q))
    print(ans)
    # print(x)


if __name__ == "__main__":
    main()
