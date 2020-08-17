from itertools import product

from functools import reduce
from operator import xor

n, k = map(int, input().split())
t = [[int(i) for i in input().split()] for j in range(n)]

ans = 'Nothing'

for qs in list(product(*t)):
    if reduce(xor, qs) == 0:
        ans = 'Found'
        break

print(ans)