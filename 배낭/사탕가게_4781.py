# gold 4

import sys

input = sys.stdin.readline

while True:
    n, m = input().split()

    if n == "0" and m == "0.00":
        break

    n = int(n)
    dollars, cents = m.split('.')
    m = int(dollars) * 100 + int(cents)

    dp = [0] * (m + 1)
    backpack = []

    for i in range(n):
        c, p = input().split()
        c = int(c)
        dollars, cents = p.split('.')
        p = int(dollars) * 100 + int(cents)

        backpack.append([c, p])
    
    
    for calories, price in backpack:
        for i in range(price, m + 1):
            dp[i] = max(dp[i], dp[i - price] + calories)
    
    print(dp[-1])
