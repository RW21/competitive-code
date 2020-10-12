t = int(input())

for test in range(t):
    n = int(input())
    x = n-2
    print(2)
    print(n-1, n)
    y = n
    for i in range(n-2):
        print(x,y)
        x-=1
        y-=1