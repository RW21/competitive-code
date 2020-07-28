def max_area(height):
    ans = 0

    l, r = 0, len(height) - 1
    while l != r:
        if height[r] > height[l]:
            area = height[l] * (r - l)
            l += 1
        else:
            area = height[r] * (r - l)
            r -= 1
        ans = max(area, ans)

    return ans


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
