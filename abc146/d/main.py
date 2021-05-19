#!/usr/bin/env python3
from collections import deque

def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append((b,i))
        adj[b].append((a,i))
    p = max([len(a) for a in adj])
    ans = [-1] * (N-1)
    visited = [-1] * N
    visited[0] = 0
    q = deque([0])
    
    while q:
        now = q.popleft()
        tmp = 0
        for v in adj[now]:
            if visited[v[0]] == 0:
                tmp = ans[v[1]]
                break
        
        for v in adj[now]:
            if visited[v[0]] < 0:
                q.append(v[0])
                ans[v[1]] = (tmp+1) % p
                tmp += 1
                visited[v[0]] = 0
                if ans[v[1]] == 0:
                    ans[v[1]] += p
    print(p)
    [print(a) for a in ans]

if __name__ == "__main__":
    main()
