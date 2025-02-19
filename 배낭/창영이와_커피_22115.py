import sys

input = sys.stdin.readline

n, total = map(int, input().split())
backpack = list(map(int, input().split()))

dp = [float('inf')] * (total + 1)
dp[0] = 0  # 0을 만드는 건 0개의 아이템 필요

# 각 아이템은 한 번씩만 사용할 수 있다고 가정
for item in backpack:
    # dp 배열을 뒤에서부터 순회해, 아이템이 중복 사용되지 않도록 함
    for i in range(total, item - 1, -1):
        if dp[i - item] != float('inf'):
            dp[i] = min(dp[i], dp[i - item] + 1)
            
print(dp[total] if dp[total] != float('inf') else -1)
