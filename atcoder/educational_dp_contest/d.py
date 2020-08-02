import numpy as np

n, w = [int(i) for i in input()]
weight, value = [], []
for i in range(n):
    w, v = [int(i) for i in input().split()]
    weight.append(w)
    value.append(v)

dp = np.zeros(w+1)

for i in range(n):
    dp[weight[i]:] = np.maximum(dp[:-weight[i]] + value[i], dp[weight[i]:])

print(dp[w])