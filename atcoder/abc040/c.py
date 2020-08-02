from math import inf

n = int(input())
a = [int(i) for i in input().split()]

dp = [inf for i in range(n)]
dp[0] = 0

for i in range(1, n):
    if i == 1:
        dp[i] = abs(a[i] - a[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(a[i] - a[i - 1]), dp[i-2] + abs(a[i] - a[i-2]))

print(dp[-1])