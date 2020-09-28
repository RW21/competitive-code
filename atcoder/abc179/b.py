n = int(input())
d1, d2 = [], []
for i in range(n):
    a, b = input().split()
    d1.append(int(a))
    d2.append(int(b))

count = 0
for a, b in zip(d1, d2):
    if a == b:
        count += 1
    else:
        count = 0
    if count == 3:
        print('Yes')
        break

if count != 3:
    print('No')