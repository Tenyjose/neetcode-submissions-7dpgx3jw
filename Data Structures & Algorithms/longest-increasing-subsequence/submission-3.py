class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        longest = 1
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
                longest+=1
            else:
                left,right = 0,len(lst)-1
                while left < right:
                    mid = (left+right)//2
                    if lst[mid] < num:
                        left = mid+1
                    else: 
                        right = mid
                lst[left] = num

        return longest