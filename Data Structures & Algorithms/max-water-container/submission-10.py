"""
PROBLEM UNDERSTANDING

Given an array of heights representing vertical lines,
find two lines that together with the x-axis form a container
that holds the maximum amount of water.

Input: Array of integers (heights of vertical lines)
Output: Integer (maximum water that can be contained)

The amount of water is calculated as:
area = width × height
where width = distance between two lines
and height = minimum of the two line heights

Constraints:
- Need at least 2 heights to form a container
- Cannot tilt the container (water level is horizontal)

Edge cases: Empty array, single element, all same heights
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        APPROACH
        
        Use two-pointer technique starting from both ends.
        
        Strategy:
        1. Place left pointer at start, right pointer at end
        2. Calculate current water capacity
        3. Move the pointer with SHORTER height inward
           (moving taller height can never improve result)
        4. Track maximum water found
        
        Why move shorter height?
        - Container height = min(left_height, right_height)
        - Moving taller height only decreases width
        - Height stays same (still limited by shorter side)
        - Can never get better result
        
        Moving shorter height:
        - Width decreases but might find taller height
        - Could potentially increase overall area
        
        Time Complexity: O(n) - single pass with two pointers
        Space Complexity: O(1) - only pointer variables
        """
        
        # Edge case: need at least 2 heights
        if len(heights) <= 1:
            return 0
        
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            # Calculate current container capacity
            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            
            # Update maximum
            max_water = max(max_water, water)
            
            # Move pointer with shorter height
            if heights[left] < heights[right]:
                left += 1
            else:  # >= case (handles equal heights too)
                right -= 1
        
        return max_water

"""
REASONING

Two-pointer approach works by always moving the limiting factor (shorter height).

Example: heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Initial: left=0 (height=1), right=8 (height=7)
  water = 8 × min(1, 7) = 8
  1 < 7 → move left

left=1 (height=8), right=8 (height=7)
  water = 7 × min(8, 7) = 49 ✓ (best so far)
  8 > 7 → move right

left=1 (height=8), right=7 (height=3)
  water = 6 × min(8, 3) = 18
  8 > 3 → move right

Continue until pointers meet...
Maximum: 49

Why this works:
By always moving the shorter height, we explore all potentially
better configurations. Moving the taller height would never
improve the result since height is limited by the shorter side.

Alternative: Brute force (check all pairs) would be O(n²), rejected.
"""
