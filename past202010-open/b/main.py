X, Y = map(int, input().split())
if Y == 0:
    print('ERROR')
    exit()
ans = "{}.{:02}".format(X//Y, (X % Y)*100//Y)
print(ans)
