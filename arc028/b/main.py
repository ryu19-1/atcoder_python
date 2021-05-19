#!/usr/bin/env python3
from bisect import bisect_right

# Binary indexed tree
class BIT():
    def __init__(self,n):
        self.array = [0] * n
        self.N = n

    # 1番目からi番目までの累積和を求める
    def sum(self,i):
        s = 0
        while i > 0:
            s += self.array[i-1]
            i -= i&(-i)
        return s

    # sum(i,j)
    def sum2(self,i,j):
        return self.sum(j) - self.sum(i-1)

    # i番目にxを追加
    def add(self,i,x):
        while i <= self.N:
            self.array[i-1] += x
            i += i&(-i)

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    


if __name__ == "__main__":
    main()
