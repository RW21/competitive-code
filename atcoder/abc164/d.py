s = [int(i) for i in input()]
s.reverse()
amari = []
b = 0
c = 0
for i in range(len(s)):
    a = (b + s[i] *(10 ** i)) % 2019
    amari.append(a)
    if a == 0:
        c += 1
    b = a
print(c + len(amari) - len(set(amari)))

