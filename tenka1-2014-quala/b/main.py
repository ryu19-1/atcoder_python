#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def cal_combo(A, combo):
    return A * (1 + combo//10 * 0.1)


def main():
    # 合計ダメージ数
    damage = 0

    # 現在のコンボ数
    combo = 0

    # ため時間
    tame = 0

    # かぶりんの使用可能までの秒数(0なら使用可能)
    load = [0] * 5

    S = input()
    N = len(S)
    for i in range(N):
        if tame == 0:
            use = []
            for j in range(5):
                if load[j] == 0:
                    use.append(j)
            # print(use)
            if S[i] == 'N':
                if len(use) >= 1:
                    # 使用可能があれば投げる
                    for j in range(1):
                        u = use[j]
                        load[u] += 6.5
                    damage += cal_combo(10, combo)
                    combo += 1
            elif S[i] == 'C':
                if len(use) >= 3:
                    for j in range(3):
                        u = use[j]
                        load[u] += 8.5
                    damage += cal_combo(50, combo)
                    # combo += 1
                    tame += 2.5
            else:
                # 入力なし
                pass
                # combo = 0
        elif tame == 0.5:
            combo += 1

        # 秒数経過処理
        for j in range(5):
            load[j] = max(0, load[j] - 1)

        tame = max(0, tame - 1)

        if S[i] != '-':
            print(i, damage, load, combo)
    print(damage)


if __name__ == "__main__":
    main()
