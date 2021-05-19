#!/usr/bin/env python3


def main():
    N = int(input())
    x = [None] * N
    y = [None] * N
    h = [None] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    
    # Cx, Cyを全探索する
    for i in range(101):
        for j in range(101):
            flag = True
            maxH = 10**12
            H = set()
            for k in range(N):
                if h[k] == 0:
                    maxH = min(maxH, abs(x[k]-i) + abs(y[k]-j))
                else:
                    tmpH = h[k] + abs(x[k]-i) + abs(y[k]-j)
                    H.add(tmpH)
                    if len(H) > 1:
                        flag = False
                        break
            if flag and list(H)[0] <= maxH:
                print(i,j,list(H)[0])

if __name__ == "__main__":
    main()
