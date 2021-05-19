#!/usr/bin/env python3
import math

def cal_primes(N):
    candidate = [*range(2, N+1)]
    primes = []

    while candidate[0]**2 <= N:
        primes.append(candidate[0])
        candidate = [*filter(lambda x: x % candidate[0] != 0, candidate)]
    
    primes.extend(candidate)
    return primes

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        if math.gcd(A[0],A[1]) == 1:
            ans = 0
        else:
            ans = 2
    else:
        A.sort()
        nums = [0] * (10**6+1)
        for a in A:
            nums[a] += 1
        
        plist = cal_primes(10**6//2)

        ans = 0
        for p in plist:
            now = p
            cnt = 0
            while now <= 10**6:
                cnt += nums[now]
                now += p
            if cnt == N:
                ans = 2
                break
            elif cnt > 1:
                ans = 1
    
    if ans == 0:
        print('pairwise coprime')
    elif ans == 1:
        print('setwise coprime')
    else:
        print('not coprime')

if __name__ == "__main__":
    main()