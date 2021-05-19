#!/usr/bin/env python3
from collections import deque


def main():
    Q, L = map(int, input().split())
    size = 0
    order = deque()
    for _ in range(Q):
        query = input().split()
        if query[0] == 'Size':
            print(size)
        elif query[0] == 'Top':
            if size == 0:
                print('EMPTY')
                return
            print(order[0][1])
        elif query[0] == 'Pop':
            N = int(query[1])
            if N > size:
                print('EMPTY')
                return
            size -= N
            while N > 0:
                p, q = order.popleft()
                if p <= N:
                    N -= p
                else:
                    order.appendleft((p-N, q))
                    N = 0
        else:
            N = int(query[1])
            M = int(query[2])
            if size + N > L:
                print('FULL')
                return
            order.appendleft((N, M))
            size += N
    print('SAFE')


if __name__ == "__main__":
    main()
