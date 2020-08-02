k = int(input())

s = '7'
count = 1

while True:
    if int(s) % k == 0:
        break
    count += 1
    s += '7'

print(count)