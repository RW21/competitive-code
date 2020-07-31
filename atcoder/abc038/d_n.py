N = int(input())
wh = [[int(j) for j in input().split()] for i in range(N)]

wh.sort(key=lambda x: (x[0], -x[1]))

print(wh)