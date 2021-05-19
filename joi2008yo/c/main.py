#!/usr/bin/env python3
from heapq import heappush, heappop
from bisect import bisect_left


def main():
    N = int(input())
    T = []
    cards = [True] * (2*N)
    for i in range(N):
        a = int(input())
        T.append(a - 1)
        cards[a - 1] = False

    H = []
    for i in range(2*N):
        if cards[i]:
            H.append(i)

    T.sort()
    H.sort()
    # print(T, H)

    turn = 0
    now = -1

    while len(T) > 0 and len(H) > 0:
        if turn % 2 == 0:  # Taro's turn
            d = bisect_left(T, now)
            if d == len(T):
                now = -1
            else:
                now = T[d]
                del T[d]
        else:
            d = bisect_left(H, now)
            if d == len(H):
                now = -1
            else:
                now = H[d]
                del H[d]
        # print(turn, now, T, H)
        turn += 1
    print(len(H))
    print(len(T))


if __name__ == "__main__":
    main()
