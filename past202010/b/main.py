def main():
    X, Y = map(int, input().split())
    if Y == 0:
        print('ERROR')
        exit()
    if X == 0:
        print('0.00')
        exit()
    res = '00'+str(1000 * X // Y)
    ans = res[:-3] + '.' + res[-3:-1]
    i = 0
    while ans[i] == '0':
        ans = ans[1:]

    print(ans)


if __name__ == "__main__":
    main()
