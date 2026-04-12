"""
PROBLEM UNDERSTANDING

Given an integer array, find all unique triplets [a, b, c] 
that sum to zero (a + b + c = 0).

Input: Array of integers (may contain duplicates)
Output: List of unique triplets that sum to zero

Constraints:
- Solution must not contain duplicate triplets
- Order of triplets doesn't matter
- Order within each triplet doesn't matter
- Array length can be 0 to 3000

Edge cases: Empty array, less than 3 elements, no valid triplets,
            all same values, many duplicates
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        APPROACH
        
        Use sorting + two pointers to find triplets efficiently.
        
        Strategy:
        1. Sort the array (enables two-pointer technique)
        2. Fix first number with outer loop (index i)
        3. Use two pointers (left, right) for remaining two numbers
        4. Skip duplicates at all three positions to avoid duplicate triplets
        
        For each fixed first number:
        - If sum < 0: Need larger sum → move left pointer right
        - If sum > 0: Need smaller sum → move right pointer left
        - If sum = 0: Found triplet! Add to result, skip duplicates, move both
        
        Duplicate handling is crucial:
        - Skip duplicate first numbers in outer loop
        - After finding triplet, skip duplicate left values
        - After finding triplet, skip duplicate right values
        - Then move both pointers one more step to next different values
        
        Time Complexity: O(n²)
        - Sorting: O(n log n)
        - Outer loop: O(n)
        - Inner two-pointer: O(n) per iteration
        - Total: O(n log n) + O(n²) = O(n²)
        
        Space Complexity: O(1) excluding output array
        - Only using pointer variables
        """
        
        res = []
        nums.sort()  # Sort to enable two-pointer approach
        
        for i in range(len(nums)):
            # Optimization: if first number > 0, impossible to sum to 0
            if nums[i] > 0:
                break
            
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Sum too small, need larger value
                    left += 1
                elif total > 0:
                    # Sum too large, need smaller value
                    right -= 1
                else:
                    # Found valid triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to next different values
                    left += 1
                    right -= 1
        
        return res

"""
REASONING

Sorting enables two-pointer technique and easy duplicate detection.

Example: nums = [-1, 0, 1, 2, -1, -4]
After sort: [-4, -1, -1, 0, 1, 2]

i=0 (nums[0]=-4):
  left=1, right=5: -4 + (-1) + 2 = -3 < 0 → left++
  left=2, right=5: -4 + (-1) + 2 = -3 < 0 → left++
  left=3, right=5: -4 + 0 + 2 = -2 < 0 → left++
  left=4, right=5: -4 + 1 + 2 = -1 < 0 → left++
  left=5, right=5: Exit (left >= right)

i=1 (nums[1]=-1):
  left=2, right=5: -1 + (-1) + 2 = 0 ✓
    Add [-1, -1, 2]
    Skip duplicates, move pointers
  left=3, right=4: -1 + 0 + 1 = 0 ✓
    Add [-1, 0, 1]
    Move pointers
  left=4, right=3: Exit

i=2 (nums[2]=-1):
  Skip (duplicate of nums[1])

i=3 onwards: No more valid triplets

Result: [[-1, -1, 2], [-1, 0, 1]] ✓


Alternative: Hash map for each pair would be O(n²) space, rejected.
Three nested loops would be O(n³) time, rejected.
"""