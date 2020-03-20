class Solution:
    def rob(self, nums) -> int:
        # edge cases
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        
        #when n>2
        
        money = [0 for i in range(len(nums))]
        money[0]=nums[0]
        money[1]=max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            money[i]=max(money[i-2]+nums[i], money[i-1])
        return money[-1]

print(Solution().rob([2,7,9,3,1]))