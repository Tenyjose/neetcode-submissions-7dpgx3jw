class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        return False if len(nums) == len(seen) else True