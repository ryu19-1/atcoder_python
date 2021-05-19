#!/usr/bin/env python3
from heapq import heappush, heappop


def main():
    N, C = map(int, input().split())
    q = []
    for i in range(N):
        s, t, c = map(int, input().split())
        # 同時刻なら開始が先になるように
        heappush(q, [s-0.5, 0, c-1])
        heappush(q, [t, 1, c-1])
    onair = [0] * C
    protect = [False] * C
    ans = 0
    while q:
        h, flag, channel = heappop(q)
        if flag == 0:
            # 番組が始まる
            if onair[channel] == 1:
                protect[channel] = True
            else:
                onair[channel] = 1
            ans = max(ans, sum(onair))
        else:
            # 番組が終わる
            if protect[channel]:
                protect[channel] = False
            else:
                onair[channel] = 0
    print(ans)


if __name__ == "__main__":
    main()
