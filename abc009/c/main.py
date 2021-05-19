N, K = map(int, input().split())
S = input()
U = sorted(list(S))
T = []
# 先頭から1文字ずつ決めていく
diff = 0
for i in range(N):
    tmpS = S[i+1:]
    for j in range(len(U)):# 仮に今の文字をuとする
        # 残りの文字のdiffがK以内であればOK
        tmpdiff = 0
        tmpU = U[:]
        u = tmpU.pop(j)
        for k in range(26):
            tmpdiff +=  abs(tmpS.count(chr(k+97)) - tmpU.count(chr(k+97)))
        tmpdiff //= 2
        if S[i] != u:
            tmpdiff += 1
        if tmpdiff + diff <= K:
            T.append(u)
            if S[i] != u:
                diff += 1
            U = sorted(tmpU)
            break
print(''.join(T))