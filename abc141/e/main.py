# Z-algorithmで解いてみる

N = int(input())
S = input()
ans = 0
for h in range(N):
    T = S[h:]
    M = len(T)
    Z = [0] * M
    c = 0
    for i in range(1, M):
        l = i - c  # 今見ている場所が計算済みcからどれだけ離れているか
        if i + Z[l] < c + Z[c]:
            Z[i] = Z[l]
        else:
            j = max(0, c + Z[c] - i)
            while i + j < M and T[j] == T[i + j]:
                j += 1
            Z[i] = j
            c = i
    # Z[0] = M
        # print(i, Z[i])
        if i >= Z[i]:
            ans = max(ans, Z[i])
print(ans)
