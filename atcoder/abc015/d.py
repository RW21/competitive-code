from pprint import pprint

w = int(input())
n, k = map(int, input().split())

dp = [[0 for i in range(w + 1)] for j in range(k + 1)]

ans = 0
for i in range(n):
    a, b = map(int, input().split())

    for limit in range(k, 0, -1):
        for width in range(w, 0, -1):
            if width - a >= 0:
                dp[limit][width] = max(dp[limit][width], dp[limit - 1][width - a] + b)
                ans = max(ans, dp[limit][width])
        pprint(dp)

print(ans)