s = input()
N = len(s)
cnt = 0
for i in range(N):
    if i % 2 == 0 and s[i] == 'p':
        cnt -= 1
    elif i % 2 == 1 and s[i] == 'g':
        cnt += 1
print(cnt)