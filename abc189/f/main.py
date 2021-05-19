#!/usr/bin/env python3


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    gotoStart = [0] * (N + 1)
    ren = int(K > 0)
    now = ren
    for i in range(1, K):
        if A[i] == A[i - 1] + 1:
            now += 1
        else:
            now = 1
        ren = max(ren, now)
    if ren >= M:
        print(-1)
        exit()
    for i in range(K):
        gotoStart[A[i]] = 1
    # f(0)=Xとして、f(i)=A*X+Bと表せるので、A,Bをdpする
    dp = [[0, 0] for _ in range(N+1)]
    cumdp = [[0, 0] for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        if gotoStart[i]:
            dp[i] = [1, 0]
        else:
            dp[i][0] += cumdp[i+1][0]
            dp[i][1] += cumdp[i+1][1]
            if i+M < N:
                dp[i][0] -= cumdp[i+M+1][0]
                dp[i][1] -= cumdp[i+M+1][1]
            dp[i][1] += 1
            # print(i, dp, cumdp)
        # 累積和を計算する
        cumdp[i][0] = cumdp[i+1][0]+dp[i][0]/M
        cumdp[i][1] = cumdp[i+1][1]+dp[i][1]/M
    ans = dp[0][1] / (1 - dp[0][0])
    print(ans)


if __name__ == "__main__":
    main()
