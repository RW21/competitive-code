n, w = map(int, input().split())
W = []
V = []

for _ in range(n):
    x, y = map(int, input().split())
    W.append(x)
    V.append(y)
dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
    for sum_w in range(w + 1):
        if W[i] > sum_w:
            dp[i + 1][sum_w] = dp[i][sum_w]
        else:
            dp[i + 1][sum_w] = max(dp[i][sum_w], dp[i][sum_w - W[i]] + V[i])

print(dp[n][w])
