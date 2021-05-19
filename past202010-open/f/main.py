from collections import Counter
N, K = map(int, input().split())
S = [input() for _ in range(N)]
l = Counter(S)
v = [*l.values()]
num = sorted(v, reverse=True)[K - 1]
if v.count(num) > 1:
    print('AMBIGUOUS')
else:
    for k, v in l.items():
        if v == num:
            print(k)
            break
