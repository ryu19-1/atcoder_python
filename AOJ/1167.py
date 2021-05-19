a = [1]
i = 2
while a[-1] <= 1e6:
    a.append(a[-1]+i*(i+1)//2)
    i += 1

INF = 1e12
N = 1e6
if N == 0:
    exit()

dp  = [0] + [INF] * N
dp2 = [0] + [INF] * N
i = 0
while a[i] <= N:
    for j in range(1,N+1):
        if j - a[i] >= 0:
            dp[j] = min(dp[j], dp[j-a[i]]+1)
            if a[i]%2 == 1:
                dp2[j] = min(dp2[j], dp2[j-a[i]]+1)
    i += 1
    
while 1:
    n = int(input())
    if n == 0:
        exit()
    print(dp[n],dp2[n])