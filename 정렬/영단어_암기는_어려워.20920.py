# silver 3

import sys
from collections import Counter

input = sys.stdin.readline

# 길이가 M 이상
# 1. 자주 나오는 단어
# 2. 길이가 길수록
# 3. 사전 순

N, M = map(int, input().split())
factory = []

for _ in range(N):
    temp = input().strip()
    if len(temp) >= M:
        factory.append(temp)

counter = Counter(factory)
factory = sorted(set(factory), key=lambda x: (-counter[x], -len(x), x))

for item in factory:
    print(item)