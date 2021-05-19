#!/usr/bin/env python3
from itertools import accumulate

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(accumulate(a))

    ans = 10**18

    for j in range(2):# 偶数行が正か奇数行が正
        ans2 = 0
        diff = 0
        for i in range(n):
            p = a[i] + diff
            # print(a[i],diff)
            if (i+j) % 2 == 0 and p <= 0:# 正になる
                ans2 += abs(p)+1
                diff += abs(p)+1
            elif (i+j) % 2 == 1 and p >= 0:# 負になる
                ans2 += abs(p)+1
                diff -= abs(p)+1

        ans = min(ans, ans2)
    print(ans)

if __name__ == "__main__":
    main()
