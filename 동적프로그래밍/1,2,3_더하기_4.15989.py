# gold 5

import sys

input = sys.stdin.readline

# 1

# 1+1
# 2

# 1+1+1
# 2+1
# 3

# 1+1+1+1
# 1+1+2
# 2+2
# 3+1

# 1+1+1+1+1
# 1+1+2+1
# 2+2+1
# 3+1+1
# 2+3

N = int(input())
targets = []

for _ in range(N):
    targets.append(int(input()))

# 1로만 만드는 경우의 수는 1개씩 존재
dp = [1] * (max(targets) + 1)

# 2를 추가해서 만드는 경우의 수는 dp[i-2]의 경우의 수에 +2를 해서 만들 수 있음
# 3: (1)+2
# 5: (1+1+1)+2, (1+2)+2
for i in range(2, len(dp)):
    dp[i] += dp[i - 2]

print(dp)

# 3을 추가해서 만드는 경우의 수는 dp[i-3]의 경우의 수에 +3을 해서 만들 수 있음
# 5: (1+1)+3, (2)+3
for i in range(3, len(dp)):
    dp[i] += dp[i - 3]

print(dp)

for target in targets:
    print(dp[target])

    
    