from collections import *
from heapq import *
N=int(input())
T=[0]*N
p=[]
q=[]
for i in range(N):
    T[i]=deque(tuple(map(int,input().split()))[1:])
    r=-T[i].popleft()
    heappush(p,(r,i))
    heappush(q,(r,i))
    if T[i]:
        heappush(q,(-T[i][0],i))
M=int(input())
A=list(map(int,input().split()))
u=set()
v=set()
for a in A:
    if a == 1:
        while 1:
            x,i=heappop(p)
            if not x in v:
                break
        print(-x)
        u.add(x)
    else:
        while 1:
            x,i=heappop(q)
            if not x in u:
                break
        print(-x)
        v.add(x)
    if T[i]:
        r=-T[i].popleft()
        heappush(p,(r,i))
        if T[i]:
            heappush(q,(-T[i][0],i))