perm = []

# 順列の生成
def make_perm(n, m = 0):
    if n == m: print(perm)
    else:
        for x in range(1, n + 1):
            if x in perm: continue
            perm.append(x)
            make_perm(n, m + 1)
            perm.pop()

print(make_perm(3))