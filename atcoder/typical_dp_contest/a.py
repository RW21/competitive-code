n = int(input())
p = list(map(int, input().split()))

width = sum(p)
dp = [[False for i in range(width + 1)] for j in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(width):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + p[i - 1]] = True

print(sum(dp[-1]))