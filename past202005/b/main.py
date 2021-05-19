#!/usr/bin/env python3

# 必要なのは各問を解いた人数が何人という情報だけで、
# 誰が解いたという情報は保持する必要ない
def main():
    N, M, Q = map(int, input().split())
    count = [0] * M
    solved = [[] for _ in range(N)]

    for i in range(Q):
        s = list(map(lambda x: int(x)-1, input().split()))
        if s[0] == 0:
            print(sum([max(0,N-count[s]) for s in solved[s[1]]]))
        elif s[0] == 1:
            solved[s[1]].append(s[2])
            count[s[2]] += 1

if __name__ == "__main__":
    main()
