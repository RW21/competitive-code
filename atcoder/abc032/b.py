s = input()
k = int(input())

res = set()

for i in range(len(s)):
    if (i + k) > len(s):
        break
    res.add(s[i:i + k])

print(len(res))
