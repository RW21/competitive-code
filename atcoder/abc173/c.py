h, w, k = [int(i) for i in input().split()]
lines = [input() for i in range(h)]
ans = 0
# bit search
for h_1 in range(1 << h):
    for w_1 in range(1 << w):
        black = 0

        for i in range(h):
            for j in range(w):
                if (h_1 >> i) & 1 == 0 and (w_1 >> j) & 1 == 0 and lines[i][j] == '#':
                    black += 1
        if black == k:
            ans += 1
print(ans)
