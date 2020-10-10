n = int(input())

s = set(range(1, n+1))
for i in  map(int, input().split()):
    s.remove(i)

print(s.pop())
