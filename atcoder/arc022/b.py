N = int(input())
A = [int(i) for i in input().split()]
ans, r = 0, 0
s = set()

for l in range(len(A)):
    while r < len(A) and A[r] not in s:
        s.add(A[r])
        r += 1

    # print(s)
    ans = max(ans, len(s))

    if l == r:
        r += 1
    else:
        s.remove(A[l])

print(ans)
