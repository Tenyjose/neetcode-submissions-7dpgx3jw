class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left,right = 0,len(nums)

        while left<right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]> target:
                right -= 1
            else:
                left +=1

        return result