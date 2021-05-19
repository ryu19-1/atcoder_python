#!/usr/bin/env python3


def main():
    N = int(input())
    a = list(map(int, input().split()))
    cost = [None] * N
    cost[0] = 0
    cost[1] = abs(a[0]-a[1])
    for i in range(2,N):
        p = cost[i-1] + abs(a[i]-a[i-1])
        q = cost[i-2] + abs(a[i]-a[i-2])
        cost[i] = min(p,q)
    print(cost[N-1])

if __name__ == "__main__":
    main()
