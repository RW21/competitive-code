# matrix chain multiplication

N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

dp = [[float('inf')]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])
