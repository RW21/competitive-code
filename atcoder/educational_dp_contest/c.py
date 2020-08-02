n = int(input())
a = [[int(i) for i in input().split()] for i in range(n)]

dp = [[-1 for i in range(3)] for j in range(n + 1)]
dp[0] = [0 for i in range(3)]

for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if j == k:
                # if same as previous day
                continue
            dp[i][j] = max(dp[i - 1][k] + a[i - 1][j], dp[i][j])

print(max(dp[-1]))