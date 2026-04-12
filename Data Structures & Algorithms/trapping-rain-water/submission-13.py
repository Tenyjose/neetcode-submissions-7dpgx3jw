"""
PROBLEM UNDERSTANDING

Given an elevation map where width of each bar is 1,
calculate how much rainwater can be trapped after raining.

Input: Array of non-negative integers representing elevation heights
Output: Total units of rainwater that can be trapped

The water trapped at each position is determined by:
- The minimum of (max height to left, max height to right)
- Minus the current height
- If negative, no water can be trapped

Constraints:
- Heights are non-negative
- Need at least 3 bars to trap water

Edge cases: Less than 3 elements, flat terrain, all descending/ascending
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        APPROACH
        
        Use two-pointer technique with tracking of max heights.
        
        Key insight:
        Water trapped at position i = min(maxLeft, maxRight) - height[i]
        
        Strategy:
        1. Start with pointers at both ends
        2. Track max height seen from left (maxLeft)
        3. Track max height seen from right (maxRight)
        4. Move pointer from side with LOWER max
        5. Calculate water at new position
        
        Why move the pointer with lower max?
        - Water level is limited by the LOWER of the two maxes
        - We know for certain the current side's max is the limiting factor
        - Safe to calculate water with that max
        
        Order matters:
        1. Move pointer first
        2. Update max for that side
        3. Calculate water (max - current_height)
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - only pointer variables
        """
        
        # Edge case: need at least 3 positions to trap water
        if len(height) <= 2:
            return 0
        
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        total_water = 0
        
        while left < right:
            if maxLeft < maxRight:
                # Process from left side (left max is limiting factor)
                left += 1  # Move pointer FIRST
                maxLeft = max(maxLeft, height[left])  # Update max
                total_water += maxLeft - height[left]  # Calculate water
            else:
                # Process from right side (right max is limiting factor)
                right -= 1  # Move pointer FIRST
                maxRight = max(maxRight, height[right])  # Update max
                total_water += maxRight - height[right]  # Calculate water
        
        return total_water

"""
REASONING

Two-pointer approach works by processing from the side with lower max height.

Example: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Initial: left=0, right=11
maxLeft=0, maxRight=1

The algorithm processes inward, calculating water at each position
based on the limiting max height (the smaller of maxLeft and maxRight).

Key insight:
- Water at position i depends on min(maxLeft[i], maxRight[i])
- We don't need to know both maxes exactly
- We only need to know which side has the lower max
- Then we can safely calculate water using that lower max

Example trace (simplified):
left=0→1: maxLeft=1, water=1-1=0
left=1→2: maxLeft=1, water=1-0=1 (trapped!)
right=11→10: maxRight=2, water=2-1=1 (trapped!)
... continues ...

Total trapped: 6 units

Why this is O(n):
Each position visited exactly once by either left or right pointer.

Alternative: Compute maxLeft and maxRight arrays separately (O(n) space),
rejected in favor of O(1) space solution.
"""