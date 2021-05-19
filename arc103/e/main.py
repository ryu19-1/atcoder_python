s = input()
N = len(s)
cnt = []
if s[0] == '0' or s[-1] == '1':
    print(-1)
    exit()
for i in range(N // 2):
    if s[i] != s[N - 2 - i]:
        print(-1)
        exit()
    else:
        if s[i] == '1':
            cnt.append(i + 1)
print(cnt)
if sum(cnt) >= N:
    print(-1)
    exit()
# 0を始点にして増やしていく
now = 2
for c in cnt:
    print(1, now)
    nowx = now
    for i in range(c-1):
        print(nowx, now + 1)
        now += 1
    now += 1
for n in range(now, N+1):
    print(1, n)
