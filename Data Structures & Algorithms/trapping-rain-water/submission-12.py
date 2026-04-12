class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <=1:
            return 0
        left,right = 0,len(height)-1
        max_water = 0
        maxLeft,maxRight = height[left],height[right]

        while left < right:
            if maxLeft < maxRight:
                max_water += maxLeft - height[left]
                left += 1
                maxLeft = max(maxLeft,height[left])
            else:
                max_water += maxRight - height[right]
                right -= 1
                maxRight = max(maxRight,height[right])

        return max_water