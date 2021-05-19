#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # L[i][j]: このマスが光る時に左方向に照らされるマスの個数
    L = [[0]*W for _ in range(H)]
    R = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(1,W):
            if S[i][j] == '.':
                if S[i][j-1] == '.': 
                    L[i][j] = L[i][j-1] + 1
            if S[i][W-j-1] == '.':
                if S[i][W-j] == '.': 
                    R[i][W-j-1] = R[i][W-j] + 1
    
    # U[i][j]: このマスが光る時に上方向に照らされるマスの個数
    U = [[0]*W for _ in range(H)]
    D = [[0]*W for _ in range(H)]

    for j in range(W):
        for i in range(1,H):
            if S[i][j] == '.':
                if S[i-1][j] == '.': 
                    U[i][j] = U[i-1][j] + 1
            if S[H-i-1][j] == '.':
                if S[H-i][j] == '.': 
                    D[H-i-1][j] = D[H-i][j] + 1
    ans = 0
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                tmp = 1
                tmp += L[i][j] + R[i][j] + U[i][j] + D[i][j]
                ans = max(tmp,ans)
    
    print(ans)
    
if __name__ == "__main__":
    main()
