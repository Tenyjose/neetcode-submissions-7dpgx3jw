class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1

        while left <= right:
            mid = numbers[left]+numbers[right]
            if mid == target:
                return [left+1,right+1]
            elif mid >target:
                right -= 1
            else:
                left += 1
        return [-1,-1] 