n = int(input())
s = input()

ans = 0

for l in range(n):
    ans = max(len(set(s[:l]).intersection(set(s[l:]))), ans)

print(ans)
