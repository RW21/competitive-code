n, m = map(int, input().split())

s, c = [], []
for i in range(m):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)

num = [0 for i in range(n)]

for si, ci in zip(s,c):
    num[si - 1] = ci


# check valid number
if m == 0:
    print(-1)
    exit()

saw_non_zero = False
for digit in num:
    if digit == 0 and not saw_non_zero:
        print(-1)
        exit()
    if digit != 0:
        saw_non_zero = True
        print(int(''.join(map(str, num))))
        exit()
