# gold 4

import sys

input = sys.stdin.readline

target, case = map(int, input().split())

backpack = []

for _ in range(case):
    backpack.append(list(map(int, input().split())))

dp = [float("inf")] * (1100 + 1)
dp[0] = 0

for i in range(1, target+100):
    for cost, num in backpack:
        if i - num >= 0:
            dp[i] = min(dp[i - num] + cost, dp[i])

print(min(dp[target:]))

        