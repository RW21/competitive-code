def longest_palindrome(s):
    s = list(s)
    ans = []
    for l in range(len(s)):
        r = l
        while r <= len(s):
            built = [s[i] for i in range(l, r)]
            print(built)
            if is_palindrome(built):
                ans = max(built, ans, key=len)
                print('ans: ', ans)

            r += 1

    return ''.join(ans)


def is_palindrome(s):
    return s == s[::-1]


longest_palindrome()
