t_h, t_a, a_h, a_a = [int(i) for i in input().split()]

turn = True
while True:
    if turn:
        a_h -= t_a
    else:
        t_h -= a_a

    turn = not turn

    if a_h <= 0:
        print('Yes')
        break
    if t_h <= 0:
        print('No')
        break

