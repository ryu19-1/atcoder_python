N = int(input())
ga, sa, ba = map(int, input().split())
gb, sb, bb = map(int, input().split())

ans = 0
for x in range(N//ga+1):
    for y in range((N-ga*x)//sa+1):
        for z in range((N-ga*x-sa*y)//ba+1):
            print(x,y,z)