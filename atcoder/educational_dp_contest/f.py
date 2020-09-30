s = list(input())
t = list(input())
if len(s) == len(t) == 0:
    print('')
    import sys
    sys.exit()


dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]

s_i, t_i = 0,0
# don't go to last row
for i in range(len(t)):
    s_i = 0
    # skip the first element
    for j in range(1, len(s)+1):
        print(s[s_i], t[t_i])
        dp[i+1][j] = max(dp[i+1][j-1], dp[i][j]) + (lambda x, y: 1 if x==y else 0)(s[s_i], t[t_i])
        s_i += 1
    t_i += 1

res = ''
i, j = len(dp)-1, len(dp[0])-1
while i > 0 and j > 0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        i -= 1
        j -= 1
        res = s[j] + res

print(res)
    
