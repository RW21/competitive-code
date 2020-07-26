N = int(input())
a = [int(i) for i in input().split()]

ans = 0

for l in range(N):
    r = l + 1
    r_ = -1
    while r < N and a[r] > a[l]:
        if r_ != -1 and a[r] <= r_:
            break
        ans += 1
        r_ = a[r]
        r += 1

print(ans + N)
