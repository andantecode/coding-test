# silver 5

import sys

input = sys.stdin.readline

# 상근이가 이기면 SK
# 창영이가 이기면 CY

# 상근이부터 시작하고 두 사람은 항상 완벽하게 플레이

# 1개 -> 3개 -> 1개로 승리
# 1개 -> 1개 -> 3개로 승리

# 1 + 4의 배수라면 상근이가 무조건 승리

# 3개 -> 1개 -> 3개
# 3개 -> 3개 -> 1개

# 3 + 4의 배수라면 상근이가 무조건 승리

num = int(input())

# if num == 1 or num == 3 or (num - 1) % 4 == 0 or (num - 3) % 4 == 0:
#     print("SK")
# else:
#     print("CY")

dp = [False] * (num + 1)

for i in range(1, num + 1):
    if i == 1 or i == 3:
        dp[i] = True
        continue

    if dp[i - 1] or dp[i - 3]:        
        dp[i] = False

    else:
        dp[i] = True

if dp[num]:
    print("SK")
else:
    print("CY")
