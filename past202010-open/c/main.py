N, M = map(int, input().split())
s = ['.'*(M+2)] + ['.' + input() + '.' for _ in range(N)] + ['.'*(M+2)]
ans = []
for i in range(N):
    for j in range(M):
        ans.append(str(sum([s[i+ii][j:j+3].count('#') for ii in range(3)])))
[print(''.join(ans[M*i:M*i+M])) for i in range(N)]
