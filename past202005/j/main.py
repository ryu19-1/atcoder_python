#!/usr/bin/env python3
from bisect import bisect_left,insort_left

def main():
    N, M = map(int, input().split())
    eaten = [0] * N# 逆順になっていることに注意
    a = list(map(int, input().split()))
    
    for i in range(M):
        b = bisect_left(eaten,a[i])
        if b == 0:
            print(-1)
        else:
            eaten[b-1] = a[i]
            print(N-b+1)

if __name__ == "__main__":
    main()
