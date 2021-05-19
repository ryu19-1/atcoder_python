#!/usr/bin/env python3

class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x,y = y,x
            self.parents[y] = x
            self.size[x] += self.size[y]

def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    
    uf = UnionFind(N)
    for _ in range(M):
        x, y = map(int, input().split())
        uf.union(x-1,y-1)
        # print(uf.parents)
    
    adj = [[] for _ in range(N)]
    for i in range(N):
        adj[uf.find(i)].append(i)
    
    ans = 0
    for i in range(N):
        tmpP = set()
        for a in adj[i]:
            tmpP.add(p[a]-1)
        # print(tmpP,set(adj[i]))
        ans += len(tmpP & set(adj[i]))
    print(ans)

if __name__ == "__main__":
    main()
