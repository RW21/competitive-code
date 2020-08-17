from math import ceil

n = int(input())
a = [int(i) for i in input().split()]

print(ceil(sum(a)/len(a)))