class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i