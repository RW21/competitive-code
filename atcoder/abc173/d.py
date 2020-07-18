n = int(input())
comforts = [int(i) for i in input().split()]
comforts.sort(reverse=True)

print(sum(comforts[:-1]))
