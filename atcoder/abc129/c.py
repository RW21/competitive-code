n, m = [int(i) for i in input().split()]

a = [1 for i in range(n+1)]
for i in range(m):
    a[int(input())] = 0

dp = [0 for i in range(n + 1)]
dp[0] = 1
if a[1]:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = a[i] * (dp[i-2] * a[i-2] + dp[i-1] * a[i-1])

print(dp[-1])
