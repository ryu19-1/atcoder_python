#!/usr/bin/env python3
import numpy as np

def main():
    N, K = map(int, input().split())
    A = np.array(input().split(),dtype=int)
    I = np.arange(N)# 電球番号を保持
    for i in range(K):
        B = np.zeros(N+1, int)
        # ユニバーサル関数(ufunc)を利用して一度に処理
        np.add.at(B, np.maximum(0,I-A),1)
        np.add.at(B, np.minimum(N,I+A+1),-1)
        A = B.cumsum()[:-1]
        if np.all(A == N):
            break
    print(*A)

if __name__ == "__main__":
    main()
