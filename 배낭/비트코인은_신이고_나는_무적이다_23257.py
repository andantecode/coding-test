# gold 3

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

targets = list(map(abs, map(int, input().split())))

k_targets = set()

for i in range(1, M + 1):
    if i == 1:
        k_targets = set(targets)
    else:
        temp = set()

        for item in k_targets:
            for target in targets:
                temp.add(item ^ target)
        
        k_targets = temp

print(max(k_targets))
