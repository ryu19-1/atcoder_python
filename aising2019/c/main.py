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
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    checked = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.' or checked[i][j]:
                continue
            queue = deque()
            queue.append((i, j))
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            black = 1  # 黒マスの数
            white = 0
            checked[i][j] = 1

            while queue:
                nowy, nowx = queue.popleft()
                for k in range(4):
                    y = nowy + dy[k]
                    x = nowx + dx[k]
                    if 0 <= y < H and 0 <= x < W:
                        if checked[y][x]:
                            continue
                        if S[y][x] != S[nowy][nowx]:
                            if S[y][x] == '.':
                                white += 1
                            else:
                                black += 1
                            queue.append((y, x))
                            checked[y][x] = 1
            # print(i, j)
            ans += black * white
            # print(checked)
    print(ans)


if __name__ == "__main__":
    main()
