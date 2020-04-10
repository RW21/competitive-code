def removeElement(nums, val):
    start, end = 0, len(nums) - 1

    while start <= end:
        if nums[start] == val:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        else:
            start += 1
        return start

a = [3, 2, 2, 3]

removeElement(a, 2)

print(a)
