n = int(input())

base = [2**i for i in range(6)]

if n > 6:
    dp = base + [0 for i in range(n - 6)]
else:
    print(base[n - 1])
    exit()


# sum of the last 6
for i in range(6, n):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]+ dp[i-4]+ dp[i-5]+ dp[i-6])% 1000000007

print(dp[n-1])