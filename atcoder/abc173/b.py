from collections import defaultdict

N = int(input())
d = defaultdict(lambda: 0)
for i in range(N):
    d[input()] += 1

print('AC x ' + str(d['AC']))
print('WA x ' + str(d['WA']))
print('TLE x ' +str(d['TLE']))
print('RE x ' + str(d['RE']))
