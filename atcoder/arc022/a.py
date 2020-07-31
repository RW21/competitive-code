import re

S = input().lower()
a = re.fullmatch(r'.*i[a-z]*c[a-z]*t[a-z]*', S)
if a:
    print('YES')
else:
    print('NO')
