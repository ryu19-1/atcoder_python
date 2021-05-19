#!/usr/bin/env python3
import sys
from queue import deque

# 机iにあるコンテナを全て管理する必要があるわけではない
# 聞かれているのは一番上のコンテナだけなのでそれだけを値として保持すれば良い
def main():
    N, Q = map(int, input().split())
    # parents[i]:i番目のコンテナの親
    parents = [-1] * N
    # tops[i]: i番目の机の一番上のコンテナ
    tops = list(range(N))

    for _ in range(Q):
        f, t, x = map(lambda x: int(x)-1, input().split())
        tops[t],tops[f],parents[x] = tops[f],parents[x],tops[t]
    
    ans = [None] * N
    for i in range(N):
        # 1番上のコンテナから辿っていく
        now = tops[i]
        while now != -1:
            ans[now] = i+1
            now = parents[now]
    [print(a) for a in ans]
    # print(parents,tops)

if __name__ == "__main__":
    main()