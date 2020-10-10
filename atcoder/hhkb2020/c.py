n = int(input())
p_arr = map(int, input().split())

s = set()
curr_min = 0
for p in p_arr:
    
    p_new = p
    if p == curr_min:
        p_new += 1
        while p_new in s:
            p_new += 1

        curr_min = p_new

    s.add(p)


    print(curr_min)