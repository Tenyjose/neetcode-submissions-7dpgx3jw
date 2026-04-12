class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        current_max = max_sum = nums[0]

        for i in range(1,len(nums)):
            current_max = max(nums[i],current_max+nums[i])
            
            if current_max > max_sum:
                max_sum = current_max

        return max_sum