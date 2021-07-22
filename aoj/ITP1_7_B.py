while True:
    n, x = map(int, (input()).split())
    if n == 0 and x == 0:
        break
    seen = set()
    ans = 0
    for i1 in range(1, n):
        for i2 in range(1,n):
            for i3 in range(1,n):
                if i1 + i2 + i3 == x:
                    
                    if i1 in seen or i2 in seen or i3 in seen:
                        continue
                    else:
                        ans += 1
                        seen.add(i1)
                        seen.add(i2)
                        seen.add(i3)
    print(ans)




