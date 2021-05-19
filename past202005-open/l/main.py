#!/usr/bin/env python3
from collections import deque
from heapq import heappop, heappush

def main():
    N=int(input())
    T=[None]*N
    n1=[]
    n2=[]
    for i in range(N):
        _, *T[i]  = deque(tuple(map(int, input().split())))
        r = -T[i].popleft()
        heappush(n1,(r, i))
        heappush(n2,(r, i))
        if T[i]:
            heappush(n2,(-T[i][0], i))# 2番目に追加するときはpopしない

    M = int(input())
    a = list(map(int, input().split()))
    u1 = set()# used1
    u2 = set()# used2
    
    for a in A:
        if a == 1:
            while 1:
                x, i = heappop(n1)
                if not x in u2:
                    break
            print(-x)
            u1.add(x)
            
        else:
            while 1:
                x, i = heappop(n2)
                if not x in u1:
                    break
            print(-x)
            u2.add(x)
        if T[i]:
            r = -T[i].popleft()
            heappush(n1,(r, i))
            if T[i]:
                heappush(n2,(-T[i][0], i))



if __name__ == "__main__":
    main()
