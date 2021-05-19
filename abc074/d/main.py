#!/usr/bin/env python3


def main():
    N = int(input())
    A = [None for _ in range(N)]
    INF = 10**12
    for i in range(N):
        A[i] = list(map(int, input().split()))

    adj = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            flag = True
            for k in range(N):
                if k == i or k == j:
                    continue
                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    exit()
                elif A[i][j] == A[i][k] + A[k][j]:
                    flag = False
                    break
            if flag:
                adj[i][j] = A[i][j]
    ans = 0
    for i in range(N):
        ans += sum(adj[i])
    print(ans//2)
    # print(adj)

if __name__ == "__main__":
    main()
