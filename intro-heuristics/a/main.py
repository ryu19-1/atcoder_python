#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = [None for _ in range(D)]
    for i in range(D):
        s[i] = list(map(int, input().split()))
    
    # 最後に開催した日
    lasts = [-1] * 26
    for d in range(D):
        # 今日の満足度低下率を計算
        satisfies = [None] * 26
        for j in range(26):
            satisfies[j] = c[j] * (d - max(0,lasts[j]))
        # print(satisfies)

        # 一番満足度の下がるやつと一番満足度が上がるやつを比較
        dindex = -1
        score = 0
        for j in range(26):
            tmp = satisfies[j] + s[d][j]
            if score < tmp:
                score = tmp
                dindex = j

        lasts[dindex] = d
        print(dindex+1)

if __name__ == "__main__":
    main()
