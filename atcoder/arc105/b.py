from math import gcd
from functools import reduce

n = int(input())
a = set(map(int, input().split()))

print(reduce(gcd, a))
