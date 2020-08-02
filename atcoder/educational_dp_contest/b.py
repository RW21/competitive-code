from math import inf

n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]

dp = [inf for i in range(n)]
dp[0] = 0

for i in range(1, n):
    for j in range(k + 1):
        if i - j >= 0:
            dp[i] = min(dp[i - j] + abs(h[i] - h[i - j]), dp[i])

print(dp[-1])
