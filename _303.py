class NumArray:

    def __init__(self, nums):
        self.sums = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]


    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+ 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


print(NumArray([-2,0,3,-5,2,-1]).sumRange(3,4)) 