p = 10**9+7
a = [None] * (N+1)
inva = [None] * (N+1)
a[0] = 1

for i in range(1, N+1):
    a[i] = i * a[i-1] % p

inva[N] = pow(a[N], p-2, p)
for i in range(N):
    inva[N-i-1] = inva[N-i] * (N-i) % p


def ncr(n, r):
    return (a[n] * inva[r] % p) * inva[n - r] % p


def main():
    N, X = map(int, input().split())
    X = abs(X)
    S = input()
    A = 0  # グーで勝てる上限
    B = 0  # チョキorパーで勝てる上限
    for i in range(N):
        if S[i] == 'S':
            A += 1
        else:
            B += 1

    # BC0 + BC1 + ... BCA を前計算
    # i回チョキorパーで勝つ場合、それ以外のB-iは
    acum_nCr = [None] * (B + 1)
    for i in range(B + 1):
        acum_nCr[i] = ncr(B, i)
        acum_nCr[i] *= pow(2, B-i, p)
        acum_nCr[i] %= p

    # 累積和を取る
    for i in range(B, 0, -1):
        acum_nCr[i-1] += acum_nCr[i]
        acum_nCr[i-1] %= p
    # print(acum_nCr)
    ans = 0
    tmpX = X
    for aa in range(A + 1):
        if aa > 0:
            tmpX = min([abs(tmpX), abs(tmpX - 1), abs(tmpX - 3)])

        if X % 2 != aa % 2:
            continue

        # aaはACaa
        res = ncr(A, aa)
        res *= pow(2, A - aa, p)
        res %= p
        # print(aa, A-aa,res)
        if (tmpX + 5) // 6 > B:
            continue
        res *= acum_nCr[(tmpX + 5) // 6] % p
        # print(aa, res)
        ans += res % p
        ans %= p
    print(ans)


if __name__ == "__main__":
    main()
