# gold 4

# i번째 요소까지 고려했을 때 만들 수 있는 값을 저장하면서 DP로 풀까?
# 근데, A_i가 엄청 큰 수라서 시간 초과날 것 같다.

# import sys
# from collections import defaultdict
# from itertools import combinations

# input = sys.stdin.readline

# size = int(input())
# backpack = defaultdict(int)
# temp_backpack = map(int, input().split())

# for item in temp_backpack:
#     backpack[item] += 1

# count = 0

# print(backpack)

# targets = list(set(num1 + num2 for num1, num2 in combinations(backpack.keys(), 2)))

# print(targets)

# for target in targets:
#     if target in backpack.keys():
#         count += backpack[target]

# print(count)

# 현재 문제점
# 어떤 수가 좋은지 판단할 때, 그 수를 함께 포함해서 더하는 경우도 포함됨
"""
6
-3 0 0 0 3 0
여기서 4가 나와야 하는데, 6이 나온다.
"""

import sys

input = sys.stdin.readline

size = int(input())
backpack = sorted(map(int, input().split()))

if size == 1:
    print(0)
    sys.exit(0)

ans = set()

for i, item in enumerate(backpack):
    lo, hi = 0, size - 1

    while lo < hi:
        tmp = backpack[lo] + backpack[hi]

        if i == lo:
            lo += 1
            continue
        elif i == hi:
            hi -= 1
            continue

        if tmp == item:
            ans.add(i)
            break
        
        elif tmp > item:
            hi = hi - 1

        else:
            lo = lo + 1

# print(ans)
print(len(ans))

        








