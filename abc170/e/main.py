#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush, heapreplace
from bisect import bisect_right, bisect_left

def main():
    N, Q = map(int, input().split())
    M = 2*10**5# 幼稚園の数
    
    # A[i]: i番目の園児のレート
    A = [None] * N

    # B[i]: i番目の園児の所属する幼稚園の番号
    B = [None] * N

    # 各幼稚園毎の幼稚園児のレートの順序つき集合
    X = [[] for _ in range(M)]

    # 最強幼稚園児のレートの順序つき集合
    Y = []

    for i in range(N):
        a, b = map(int, input().split())
        A[i], B[i] = a,b
        heappush(X[b-1],-a)

    for j in range(M):
        if X[j]:
            # 結局heapqも配列なのでIndexで取れる
            heappush(Y, X[j][0])

    print(A,B)
    print(X)
    print(Y)
    for _ in range(Q):
        # c:転園する園児の番号
        # d:転園先の幼稚園の番号
        c, d = map(lambda x: int(x)-1, input().split())

        # 最強園児集合の幼稚園B[c]の記録を削除
        i = bisect_left(Y,A[c])
        print(Y,A[c],i)
        del Y[i]

        # 最強園児集合の幼稚園Dの記録を削除
        i = bisect_left(Y,X[D])
        del Y[i]
        
        # 園児cを幼稚園bから削除
        j = bisect_left(X[B[c]],A[c])
        del X[B[c]][j]

        # 園児cを幼稚園Dへ追加
        heappush(X[D],A[c])

        # 最強園児集合の幼稚園B[c]の記録を追加
        heappush(Y,X[B[c]][0])

        # 最強園児集合の幼稚園B[c]の記録を追加
        heappush(Y,X[D][0])

        # 園児cの所属する幼稚園番号を更新
        B[c] = D

        print(Y[-1])



if __name__ == "__main__":
    main()
