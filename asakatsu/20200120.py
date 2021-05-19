s = input()
N = len(s)
if N == 2 and s[0] == s[1]:
    print(1, 2)
else:
    for i in range(N - 2):
        res = s[i:i + 3]
        if res[0] == res[1] or res[1] == res[2] or res[0] == res[2]:
            print(i+1, i+3)
            exit()
    print(-1, -1)
