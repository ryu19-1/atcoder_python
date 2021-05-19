#!/usr/bin/env python3
from collections import deque
from random import randint
import time


def main():
    Hs = [100, 500, 1000, 2000]
    Ws = [100, 500, 1000, 2000]

    for H in Hs:
        for W in Ws:
            if H > W:
                continue
            print('H={0}, W={1}'.format(H, W))

            ## 1: 隣接リストを持っておかない ##
            elapsed_time = 0
            adj = [[] for _ in range(W * H)]
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            queue = deque([0])
            visit = [-1] * (W * H)
            visit[0] = 0

            while queue:
                now = queue.popleft()
                # 隣接
                i = now // W
                j = now % W
                start = time.time()
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < H and 0 <= x < W:
                        if visit[W * y + x] < 0:
                            queue.append(W * y + x)
                            visit[W * y + x] = visit[now] + 1
                elapsed_time += time.time() - start
            print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

            ## 2: 隣接リストを持っておく ##
            elapsed_time = 0
            adj = [[] for _ in range(W * H)]
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(H):
                for j in range(W):
                    for k in range(4):
                        y = i + dy[k]
                        x = j + dx[k]
                        if 0 <= y < H and 0 <= x < W:
                            adj[W * i + j].append(W * y + x)
            queue = deque([0])
            visit = [-1] * (W * H)
            visit[0] = 0

            while queue:
                now = queue.popleft()
                # 隣接
                i = now // W
                j = now % W
                start = time.time()
                for u in adj[now]:
                    if visit[u] < 0:
                        queue.append(u)
                        visit[u] = visit[now] + 1
                elapsed_time += time.time() - start
            print("elapsed_time2:{0}".format(elapsed_time) + "[sec]")


if __name__ == "__main__":
    main()
