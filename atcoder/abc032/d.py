N, W = [int(i) for i in input().split()]

v, w = [], []
for i in range(N):
    v_, w_ = [int(j) for j in input().split()]
    v.append(v_)
    w.append(w_)

table = [[0 for i in range(W + 1)] for j in range(N + 1)]

for i in range(N+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif w[i-1] <= j:
            table[i][j] = max(v[i-1] + table[i-1][j-w[i-1]], table[i-1][j])
        else:
            table[i][j] = table[i-1][j]

print(table[N][W])


