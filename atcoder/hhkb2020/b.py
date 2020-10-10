h, w = map(int, input().split())

s = [list(input()) for i in range(h)]

ans = 0
for i in range(h):
    for j in range(0, w):
        if i == 0:
            if j != 0 and s[i][j] == s[i][j-1] == '.':
                ans += 1
        else:
            if j != 0 and s[i][j] == s[i][j-1] == '.' :
                ans += 1
            if s[i][j] == s[i-1][j] == '.':
                ans += 1

print(ans)
            