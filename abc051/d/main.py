#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    INF = 10 ** 12
    d = [[INF] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0

    adj = [[] for _ in range(N)]
    ab = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a-1].append((c, b-1))
        adj[b - 1].append((c, a - 1))
        d[a - 1][b - 1] = c
        d[b - 1][a - 1] = c
        ab.append((a-1, b-1, c))

    # print(adj)
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][k] + d[k][j], d[i][j])

    # print(d)

    for i in range(M):
        if d[ab[i][0]][ab[i][1]] < ab[i][2]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
