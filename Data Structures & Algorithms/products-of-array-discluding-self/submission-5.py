"""
PROBLEM UNDERSTANDING

Given an integer array nums, return an array where output[i] is 
the product of all elements except nums[i].

Input: Array of integers
Output: Array of products

Constraints:
    - Each product is guaranteed to fit in integer
    - At least 2 elements in array
    - Cannot use division operator
    - Values range between -30 and 30

Edge cases: Negative numbers, zeros in array
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        APPROACH

        Two-pass solution using prefix and postfix products:
        
        Pass 1 (left to right): Store product of all elements to the left
        Pass 2 (right to left): Multiply by product of all elements to the right
        
        For each position i:
        - result[i] = (product of elements before i) × (product of elements after i)
        
        Use running prefix/postfix variables to avoid extra arrays.
        
        Time: O(n) - two passes
        Space: O(1) - excluding output array
        """
        
        # Initialize result array with 1s (for multiplication)
        res = [1] * len(nums)
        
        # Pass 1: Calculate prefix products (left to right)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # Product of all elements before i
            prefix *= nums[i]  # Update prefix for next iteration
        
        # Pass 2: Multiply by postfix products (right to left)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply by product of all elements after i
            postfix *= nums[i]  # Update postfix for next iteration
        
        return res

"""
REASONING

This works by calculating products in two passes:
- Left pass: Each position gets product of all elements to its left
- Right pass: Multiply by product of all elements to its right

Example: nums = [1,2,4,6]

Pass 1 (prefix, left to right):
- i=0: res[0]=1 (no elements before), prefix=1×1=1
- i=1: res[1]=1 (prefix=1), prefix=1×2=2
- i=2: res[2]=2 (prefix=2), prefix=2×4=8
- i=3: res[3]=8 (prefix=8), prefix=8×6=48
After pass 1: res = [1, 1, 2, 8]

Pass 2 (postfix, right to left):
- i=3: res[3]=8×1=8 (no elements after), postfix=1×6=6
- i=2: res[2]=2×6=12, postfix=6×4=24
- i=1: res[1]=1×24=24, postfix=24×2=48
- i=0: res[0]=1×48=48, postfix=48×1=48
After pass 2: res = [48, 24, 12, 8] ✓

Verification:
- res[0] = 2×4×6 = 48 ✓
- res[1] = 1×4×6 = 24 ✓
- res[2] = 1×2×6 = 12 ✓
- res[3] = 1×2×4 = 8 ✓

This avoids division and uses O(1) extra space.
"""