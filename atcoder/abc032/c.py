N, K = [int(i) for i in input().split()]
s = []
for i in range(N):
    n = int(input())
    if n == 0:
        print(N)
        exit()

    else:
        s.append(n)

ans = 0

for l in range(N):
    r, product = l, 1
    while r < N and product * s[r] <= K:
        product *= s[r]
        r += 1
    ans = max(ans, r - l)

print(ans)
