n = int(input())
h = [int(i) for i in input().split()]

dp = [0, abs(h[1] - h[0])] + [-1 for i in range(n - 2)]

for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[-1])
