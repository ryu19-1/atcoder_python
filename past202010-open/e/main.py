from itertools import permutations
N = int(input())
S = tuple(input())
for T in permutations(S, N):
    if T == S or T[::-1] == S:
        continue
    print(''.join(T))
    exit()
print('None')