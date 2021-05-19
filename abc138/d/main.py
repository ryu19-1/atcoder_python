import sys
input = sys.stdin.readline #for input speed
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
adj = [[] for _ in range(N)]
v_count = [0] * N

def DFS(v, parent):
  for u in adj[v]:
    if u != parent:
      v_count[u] += v_count[v]
      DFS(u,v)

for i in range(N-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  adj[a].append(b)
  adj[b].append(a)# aがbの親とは限らないため

for j in range(Q):
  p, x = map(int, input().split())
  v_count[p-1] += x

# 0起点に親ノードの数字を子ノードに足していく
DFS(0, -1)# 現在のノード, 親ノード
print(*v_count)