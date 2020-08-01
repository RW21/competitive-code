n = int(input())
s = [int(i) for i in input().split()]

ans, r = 0, 0
curr_sum = 0
for l in range(n):
    r = l
    while r < n and curr_sum ^ s[r] == curr_sum + s[r]:
        curr_sum += s[r]
        r += 1

    ans += r - l

    if l == r:
        r += 1
    else:
        curr_sum -= s[l]

print(ans)
