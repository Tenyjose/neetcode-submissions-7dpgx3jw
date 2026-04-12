class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left,right = 0,len(height)-1
        leftMax,rightMax = height[left],height[right]
        maxArea = 0

        while left < right:
            if leftMax < rightMax:
                maxArea += leftMax - height[left]
                left += 1
                leftMax = max(leftMax,height[left])
            else:
                maxArea += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax,height[right])


        return maxArea