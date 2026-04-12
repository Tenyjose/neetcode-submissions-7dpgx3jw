"""
PROBLEM UNDERSTANDING

Given an array of heights, I have to choose two elements 
which are heights, which form the container that holds the most
amount of water.

Input :
    - An array of heights

Output:
    - I have to return the maximum amount of water that can be stored.

Constarints:
    - I have to choose two bars that forms the container that
    hold most water.
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        APPROACH
        
        I can use a two pointer approach, and I will start from
        ends and check for the max.


        """
        if len(heights) <=1:
            return 0

        left  = 0
        right = len(heights)-1
        max_water = 0
        while left < right:
            width = right-left
            water = width*min(heights[left],heights[right])
            max_water =  max(max_water,water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return max_water
        