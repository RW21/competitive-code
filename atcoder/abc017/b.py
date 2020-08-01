x = input()

if not x:
    print('YES')
    exit()

for i in range(len(x)):
    if x[i] == 'h' and x[i - 1] == 'c':
        continue

    if not (x[i] == 'o' or x[i] == 'k' or x[i] == 'u' or (i + 2 < len(x) and x[i:i+2] == 'ch')):
        print('NO')
        exit()

print('YES')


