t = int(input())

def combination(n, t):
    return n - t + 1

for i in range(t):
    n, a, b = map(int, input().split())
    ans = 0
    for x in range(n):
        if (n - x) > a and (n - a) >= b:
            ans += 1
