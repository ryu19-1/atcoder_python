N = int(input())
X = [None] * N
Y = [None] * N
P = [None] * N
INF = 10**12

def solve():
    xsel = [[None]*N for _ in range(1<<N)]
    ysel = [[None]*N for _ in range(1<<N)]

    for i in range(2**N):
        for j in range(N):
            xsel[i][j] = abs(X[j])
            ysel[i][j] = abs(Y[j])
            for k in range(N):
                if i>>k & 1:
                    xsel[i][j] = min(xsel[i][j], abs(X[j]-X[k]))
                    ysel[i][j] = min(ysel[i][j], abs(Y[j]-Y[k]))
    
    ans = [INF] * (N+1)
    for i in range(1<<N):
        cnt = 0
        for j in range(N):
            if i>>j & 1:
                cnt += 1
        
        for j in range(i,-1,-1):
            j &= i
            cost = 0
            for k in range(N):
                if not (i>>k & 1):
                    cost += min(xsel[j][k], ysel[i-j][k]) * P[k]
            
            ans[cnt] = min(ans[cnt],cost)

    return ans


def main():
    for i in range(N):
        X[i], Y[i], P[i] = map(int, input().split())
    [print(s) for s in solve()]

if __name__ == "__main__":
    main()