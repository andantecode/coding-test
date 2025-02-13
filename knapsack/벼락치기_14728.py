# gold 5

import sys

input = sys.stdin.readline

number_of_chapters, total_time = map(int, input().split())

backpack = []

dp = [0] * (total_time + 1)

for _ in range(number_of_chapters):
    backpack.append(list(map(int, input().split())))

for i in range(number_of_chapters):
    weight, value = backpack[i]
    
    # total_time부터 weight까지 역순으로 탐색하며 값 갱신
    for time in range(total_time, weight - 1, -1):
        dp[time] = max(dp[time], dp[time - weight] + value)

print(max(dp))