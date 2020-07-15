import sys
fruits = set()
for i, line in enumerate(sys.stdin):
    if i != 0:
        fruits.add(line)

print(len(fruits))