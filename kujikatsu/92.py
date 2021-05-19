from math import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [a//2 for a in A]
LCM = 1
for i in range(N):
    LCM = LCM * B[i] // gcd(LCM, B[i])
for i in range(N):
    if LCM // B[i] % 2 == 0:
        print(0)
        exit()
print((M//LCM + 1)//2)
