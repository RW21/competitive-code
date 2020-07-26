d1 = [int(i) for i in input().split()]
d2 = [int(i) for i in input().split()]

for d in d2:
    if d in d1:
        print('YES')
        exit()

print('NO')