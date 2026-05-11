class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:  # stop when left and right converge on the answer
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # mid is in the LEFT portion (larger values)
                # minimum must be somewhere to the RIGHT of mid
                # example: [5,6,|1|,2,3,4] → mid=6, right=4 → min is right of mid
                left = mid + 1
            else:
                # mid is in the RIGHT portion (smaller values)
                # minimum is at mid or somewhere to the LEFT of mid
                # we keep mid in consideration so right = mid, not mid-1
                # example: [5,6,1,|2|,3,4] → mid=2, right=4 → min is left of mid
                right = mid
        
        # left and right have converged → this is the minimum
        return nums[left]
