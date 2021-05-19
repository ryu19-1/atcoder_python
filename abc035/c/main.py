#!/usr/bin/env python3
from itertools import accumulate


def main():
    N, Q = map(int, input().split())
    ans = [0] * (N+1)  # 全部0
    for i in range(Q):
        l, r = map(lambda x: int(x)-1, input().split())
        ans[l] += 1
        ans[r+1] -= 1
    a = list(accumulate(ans))[:-1]
    print(''.join(map(lambda x: str(x%2), a)))


if __name__ == "__main__":
    main()
