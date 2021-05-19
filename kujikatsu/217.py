r1, c1, r2, c2 = map(int, input().split())
p = 10**9 + 7
ans = 0
start = 1


# 各行
rows = []
for i in range(r2, r1-1, -1):
    res = (r2 - i + 1) * (c2 - c1 + 1) % p
    rows.append(res)
    if i > r1:
        ans += res
    else:
        ans += sum(rows)

# 各列
cols = []
for i in range(c2, c1-1, -1):
    res = (c2 - i + 1) * (r2 - r1 + 1) % p
    cols.append(res)
    if i > c1:
        ans += cols
    else:
        ans += sum(cols)
print(ans % p)
