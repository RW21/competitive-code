n, d = map(int, input().split())
two = 0
three = 0
five = 0
while d % 2 == 0:
    d //= 2
    two += 1
while d % 3 == 0:
    d //= 3
    three += 1
while d % 5 == 0:
    d //= 5
    five += 1

if d > 1:
    ans = 0
else:
    dp = [[[[0.0 for i in range(five + 1)] for j in range(three + 1)] for k in range(two + 1)] for l in range(n + 1)]
    dp[0][0][0][0] = 1.
    for i in range(n):
        for j in range(two + 1):
            for k in range(three + 1):
                for l in range(five + 1):
                    dp[i + 1][j][k][l] += dp[i][j][k][l] / 6
                    dp[i + 1][min(j + 1, two)][k][l] += dp[i][j][k][l] / 6
                    dp[i + 1][j][min(k + 1, three)][l] += dp[i][j][k][l] / 6
                    dp[i + 1][min(j + 2, two)][k][l] += dp[i][j][k][l] / 6
                    dp[i + 1][j][k][min(l + 1, five)] += dp[i][j][k][l] / 6
                    dp[i + 1][min(j + 1, two)][min(k + 1, three)][l] += dp[i][j][k][l] / 6
    ans = dp[n][two][three][five]
print(ans)
