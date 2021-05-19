import sys
sys.setrecursionlimit(10**6)


def DFS(now, arr, ans):
    if now == 13:
        arr.sort()
        res = 10 ** 9
        for k in range(len(arr) - 1):
            res = min(res, arr[k + 1] - arr[k])
        ans[0] = max(ans[0], res)
    else:
        if Time[now] == 0:
            DFS(now + 1, arr, ans)
        elif Time[now] == 1:
            DFS(now + 1, arr + [now], ans)
            DFS(now + 1, arr + [24-now], ans)
        else:
            DFS(now + 1, arr + [now, 24-now], ans)


N = int(input())
D = list(map(int, input().split()))
Time = [0] * 13
for i in range(N):
    Time[D[i]] += 1

if Time[0] > 0 or len(list(filter(lambda x: x > 2, Time))) > 0:
    print(0)
    exit()

ans = [0]
arr = [0, 24]
DFS(1, arr, ans)
print(ans[0])
