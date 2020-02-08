from typing import List

def search_insert_binary_search(nums: List[int], target: int) -> int:
    high = len(nums) - 1
    low = 0
    if nums[-1] < target:
        return len(nums)
    
    if nums[-1] == target:
        return len(nums) - 1
    
    if nums[0] >= target:
        return 0

    while high >= low:
        mid = (low + high) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[mid - 1] < target:
                return mid
            high = mid - 1
        else:
            if nums[mid + 1] > target:
                return mid + 1
            low = mid + 1

# print(search_insert_binary_search([0,1,2, 3,4,5,6,7,8], 7))
print(search_insert_binary_search([1,4,6,7,8,9],6))

def searchInsert(nums: List[int], target: int) -> int:
    # edge cases
    if target <= nums[0]:
        return 0

    if target == nums[len(nums) - 1]:
        return len(nums) - 1
    if target > nums[len(nums) - 1]:
        return len(nums)

    for i, num in enumerate(nums):
        if i != len(nums) - 1:
            if num == target:
                return i
            if num < target < nums[i + 1]:
                return i + 1


