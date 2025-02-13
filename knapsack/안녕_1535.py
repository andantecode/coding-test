# silver 2

import sys

input = sys.stdin.readline

total_health = 100
# total_happiness = 0

number_of_people = int(input())

health_list = list(map(int, input().split()))
happiness_list = list(map(int, input().split()))

backpack = list(zip(health_list, happiness_list))

# 0/1 knapsack
# DP Table: i개 요소까지 고려했을 때, 특정 health일 때 최댓값
dp = [[0] * (total_health + 1) for _ in range(number_of_people + 1)]

for i in range(1, number_of_people + 1):
    health, happiness = backpack[i - 1]

    for temp_health in range(total_health):
        if health <= temp_health:
            # i번째 요소까지 고려하며 temp_health에 넣을 값
            # i-1번째 요소까지 고려하며 temp_health에 있던 값과 그 값에서 현재 요소를 넣기 위한 요건(dp[i-1][temp_health-health] + happiness)간의 최댓값
            dp[i][temp_health] = max(dp[i - 1][temp_health], dp[i - 1][temp_health - health] + happiness)

        else:
            dp[i][temp_health] = dp[i - 1][temp_health]

print(max(dp[number_of_people]))
  