# gold 5

import sys

input = sys.stdin.readline

length = int(input())

items = []

for _ in range(length):
    items.append(list(map(int, input().split())))

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(1, length + 1):

    item0 = max(max_dp[0], max_dp[1]) + items[i-1][0]
    item1 = max(max_dp[0], max_dp[1], max_dp[2]) + items[i-1][1]
    item2 = max(max_dp[1], max_dp[2]) + items[i-1][2]

    max_dp = [item0, item1, item2]

    item0 = min(min_dp[0], min_dp[1])  + items[i-1][0]
    item1 = min(min_dp[0], min_dp[1], min_dp[2])  + items[i-1][1]
    item2 = min(min_dp[1], min_dp[2])  + items[i-1][2]

    min_dp = [item0, item1, item2]

print(max(max_dp), min(min_dp))
        
    




