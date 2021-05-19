#!/usr/bin/env python3
from collections import Counter

def main():
    S = input()
    N = len(S)
    T = [0] * (N+1)
    
    for i in range(N-1,-1,-1):
        T[i] = (T[i+1] + int(S[i]) * pow(10,N-i,2019)) % 2019
    l = Counter(T)
    ans = 0
    for v in l.values():
        ans += v * (v-1) // 2
    print(ans)

if __name__ == "__main__":
    main()
