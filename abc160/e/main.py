#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    X, Y, A, B, C = map(int, input().split())
    p = sorted(list(map(int, input().split())), reverse=True)
    q = sorted(list(map(int, input().split())), reverse=True)
    r = sorted(list(map(int, input().split())), reverse=True)

    now = sum(p[:X]) + sum(q[:Y])
    ans = now
    i = X-1
    j = Y-1

    for k in range(min(C,X+Y)):
        if i < 0:
            now += r[k]-q[j]
            j -= 1
        elif j < 0:
            now += r[k]-p[i]
            i -= 1
        elif p[i] < q[j]:
            now += r[k]-p[i]
            i -= 1
        else:
            now += r[k]-q[j]
            j -= 1
        ans = max(ans,now)
    print(ans)

if __name__ == "__main__":
    main()
