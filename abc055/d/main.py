N = int(input())
S = input()
# Sheep:0, Wolf:1
for s in range(2):
    for t in range(2):
        T = [None] * N
        T[0] = s
        T[1] = t
        for j in range(1, N-1):
            if (T[j] == 0) == (S[j] == 'o'):
                T[j + 1] = T[j-1]
            else:
                T[j + 1] = 1 - T[j-1]

        if ((T[N - 1] == 0) == (S[N - 1] == 'o')) == (T[N - 2] == T[0]):
            if ((s == 0) == (S[0] == 'o')) == (T[N - 1] == t):
                ans = [None] * N
                for i in range(N):
                    ans[i] = ['S', 'W'][T[i]]
                print(''.join(ans))
                exit()
print(-1)
