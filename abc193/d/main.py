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
    K = int(input())
    S = input()
    T = input()
    # それぞれのカードの残り枚数
    remind = [K] * 9
    takahashi = [0] * 9
    aoki = [0] * 9
    for i in range(4):
        s = int(S[i])
        remind[s - 1] -= 1
        takahashi[s - 1] += 1
        t = int(T[i])
        remind[t - 1] -= 1
        aoki[t - 1] += 1
    # print(remind)
    ans = 0
    # t_score = 0
    # for i in range(1, 10):
    #     t_score += i * pow(10, takahashi[i-1])
    # a_score = 0
    # for i in range(1, 10):
    #     a_score += i * pow(10, aoki[i-1])

    bunbo = sum(remind) * (sum(remind)-1)//2
    for i in range(1, 10):  # 高橋君の5枚目
        for j in range(1, 10):  # 青木君の5枚目
            if i == j and remind[i-1] < 2:
                continue
            elif remind[i-1] < 1 or remind[j-1] < 1:
                continue
            else:
                tmpT = takahashi[:]
                tmpT[i - 1] += 1
                tmpA = aoki[:]
                tmpA[j - 1] += 1

                t_score = 0
                for k in range(1, 10):
                    t_score += k * pow(10, tmpT[k-1])
                a_score = 0
                for k in range(1, 10):
                    a_score += k * pow(10, tmpA[k - 1])

                if t_score > a_score:
                    # print(i, j)
                    res = 0
                    if i == j:
                        res = remind[i-1] * (remind[i-1] - 1)/2
                    else:
                        res = remind[i-1] * remind[j-1]/2
                    ans += res / bunbo
    print(ans)


if __name__ == "__main__":
    main()
