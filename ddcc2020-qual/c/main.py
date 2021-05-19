#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W, K = map(int, input().split())
    s = [None] * H
    for i in range(H):
        s[i] = input()

    preR = [1] * W
    start = 1
    flag = False
    ans = [None] * H
    for i in range(H):
        count = 0
        tmpR = [start] * W
        for j in range(W):
            if s[i][j] == '#':
                if count > 0:
                    tmpR[j] += count
                count += 1
            else:
                tmpR[j] += max(0,count-1)
        # print('count',count)
        if i == 0:
            if count == 0:
                flag = True
            else:
                ans[0] = tmpR
                start += count
                preR = tmpR
        else:
            if count == 0:
                if flag:
                    pass
                else:
                    ans[i] = preR
            else:
                ans[i] = tmpR
                if flag:
                    for k in range(i):
                        ans[k] = tmpR
                    flag = False
                start += count
                preR = tmpR
    [print(*ans[i]) for i in range(H)]

if __name__ == "__main__":
    main()
