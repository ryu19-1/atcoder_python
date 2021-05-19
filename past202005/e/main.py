#!/usr/bin/env python3


def main():
    N, M, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    c = list(map(int, input().split()))
    
    for _ in range(Q):
        s = list(map(lambda x: int(x)-1, input().split()))
        if s[0] == 0:
            print(c[s[1]])
            for v in adj[s[1]]:
                c[v] = c[s[1]]
        else:
            print(c[s[1]])
            c[s[1]] = s[2] + 1

if __name__ == "__main__":
    main()
