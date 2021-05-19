N = int(input())
a = [int(input()) for _ in range(N)]
B = sorted(set(a))
dict = {}
for i in range(len(B)):
    dict[B[i]] = i
for i in range(N):
    print(dict[a[i]])
