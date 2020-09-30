n = int(input())

def solve(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    if c == 8 and num % 2 == 1:
        return True
    return False

count = 0
for i in range(1, n + 1):
    if solve(i):
        count += 1

print(count)