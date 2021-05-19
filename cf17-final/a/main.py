#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    S = input()
    T = ['AKIHABARA','KIHABARA','AKIHBARA','AKIHABRA','AKIHABAR',
        'KIHBARA','KIHABRA','KIHABAR','AKIHBRA','AKIHBAR','AKIHABR',
        'KIHBRA','KIHBAR','KIHABR','AKIHBR','KIHBR']
    if S in T:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
