t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    n = list(map(int, input().split()))

    n.sort(reverse=True)

    for i in range(1, len(n)):
        if k > 0:
            n[0] += n[i]
        k -= 1

    print(n[0])


    