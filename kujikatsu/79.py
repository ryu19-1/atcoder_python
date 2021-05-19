N = int(input())
csf = [list(map(int, input().split())) for _ in range(N-1)]
ans = [None]*N
for i in range(N-1):
    now = 0
    for j in range(i,N-1):
        if now <= s:
            now = s
        else:
            t  = (now-s+f-1)//f
            now = s + t*f
        now += c
    ans.append(now)

print(ans)