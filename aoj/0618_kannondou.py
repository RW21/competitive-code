from math import ceil

dp = [0 for i in range(30)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, len(dp)):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(dp)

while True:
    n = int(input())
    if n == 0:
        break
    combinations = dp[n]
    print(ceil(combinations / 10 / 365))
