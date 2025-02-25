# gold 3

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memory = list(map(int, input().split()))

cost = list(map(int, input().split()))

dp = [0] * (sum(cost) + 1)

for m, c in zip(memory, cost):
    for j in range(len(dp) - 1, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + m)
    
for i, item in enumerate(dp):
    if item >= M:
        print(i)
        break
