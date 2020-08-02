from math import sqrt

n, d = [int(i) for i in input().split()]

ans = 0

for i in range(n):
    x, y = [int(i) for i in input().split()]
    if sqrt(x ** 2 + y ** 2) <= d:
        ans += 1

print(ans)