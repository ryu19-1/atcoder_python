#!/usr/bin/env python3


def main():
    H, W = map(int, input().split())
    INF = 10**12
    c = [None for _ in range(10)]
    for i in range(10):
        c[i] = list(map(int, input().split()))

    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k]+c[k][j])
    
    ans = 0
    for i in range(H):
        A = list(map(int, input().split()))
        for j in range(W):
            if A[j] != -1:
                ans += c[A[j]][1]
    print(ans)

if __name__ == "__main__":
    main()
