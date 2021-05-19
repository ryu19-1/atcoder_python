#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, Q = map(int, input().split())
    h = list(map(int, input().split()))
    hdiff_even = [None] * (N // 2)
    even_dict = defaultdict(int)
    hdiff_odd = [None] * ((N-1)//2)
    odd_dict = defaultdict(int)
    ans = 0
    for i in range(N - 1):
        tmp = h[i + 1] - h[i]
        if i % 2 == 0:
            hdiff_even[i // 2] = tmp
            even_dict[tmp] += 1
        else:
            hdiff_odd[i // 2] = tmp
            odd_dict[tmp] += 1
        if tmp == 0:
            ans += 1

    even = 0
    odd = 0
    # print(hdiff_even, even_dict)
    # print(hdiff_odd, odd_dict)
    # print(hdiff_even, hdiff_odd, even, odd)

    for _ in range(Q):
        query = list(map(int, input().split()))
        # print(query)
        if query[0] == 2:
            # 奇数(0-index)がv増える
            # print(even_dict, odd_dict, even, odd)
            v = query[1]
            ans += odd_dict[v + (odd - even)]
            # print(ans)
            ans -= odd_dict[(odd - even)]
            # print(ans)
            ans += even_dict[-v - (odd - even)]
            # print(ans)
            ans -= even_dict[-(odd-even)]
            # 更新
            odd += v
        elif query[0] == 1:
            # 偶数(0-index)がv増える
            # even_dictが-v
            # print(even_dict, odd_dict)
            v = query[1]
            ans += even_dict[v - (odd - even)]
            # print(ans)
            ans -= even_dict[-(odd - even)]
            # print(ans)
            ans += odd_dict[-v + (odd - even)]
            # print(ans)
            ans -= odd_dict[(odd-even)]
            # 更新
            even += v
        else:
            # マンションuの前後だけみる
            u = query[1]
            u -= 1
            v = query[2]
            # print(u, v)
            if u < N-1:
                # print(u)
                if u % 2 == 0:
                    diff = hdiff_even[u // 2] + (odd - even)
                    even_dict[hdiff_even[u//2]] -= 1
                    hdiff_even[u // 2] -= v
                    even_dict[hdiff_even[u//2]] += 1
                else:
                    diff = hdiff_odd[u // 2] - (odd - even)
                    odd_dict[hdiff_odd[u//2]] -= 1
                    hdiff_odd[u // 2] -= v
                    odd_dict[hdiff_odd[u//2]] += 1
                if diff == 0:
                    ans -= 1
                if diff == v:
                    ans += 1

            if u > 0:
                u -= 1
                if u % 2 == 0:
                    diff = hdiff_even[u // 2] + (odd - even)
                    even_dict[hdiff_even[u//2]] -= 1
                    hdiff_even[u // 2] += v
                    even_dict[hdiff_even[u//2]] += 1
                else:
                    diff = hdiff_odd[u // 2] - (odd - even)
                    odd_dict[hdiff_odd[u//2]] -= 1
                    hdiff_odd[u // 2] += v
                    odd_dict[hdiff_odd[u // 2]] += 1
                if diff == 0:
                    ans -= 1
                if diff == -v:
                    ans += 1
        print(ans)
        # print(hdiff_even, even)
        # print(even_dict, odd_dict)


if __name__ == "__main__":
    main()
