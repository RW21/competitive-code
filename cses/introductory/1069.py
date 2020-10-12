s = input()

max_ = 0
curr_max = 0
prev = ''
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        curr_max += 1
    else:
        if curr_max > max_:
            max_ = curr_max
            curr_max = 0

if max_ == 0:
    print(curr_max)
else:
    print(max_ + 1)
