#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # ヒストグラム内最大長方形探索による解法(O(N))
    A.append(0)  # 番兵
    stack = deque()
    for i in range(N + 1):
        current_h = A[i]
        if len(stack) == 0:
            stack.append(([current_h, i]))
        else:
            if stack[-1][0] <= current_h:
                stack.append([current_h, i])
            else:
                new_i = i
                while stack and stack[-1][0] > current_h:
                    s = stack.pop()
                    new_i = s[1]
                    ans = max(ans, (i - new_i) * s[0])
                stack.append([current_h, new_i])

    # for i in range(N):
    #     cnt = 1
    #     now = A[i]
    #     ans = max(ans, now)
    #     while i+cnt < N:
    #         now = min(now, A[i + cnt])
    #         cnt += 1
    #         ans = max(ans, now*cnt)
    print(ans)


if __name__ == "__main__":
    main()
