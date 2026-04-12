class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                # Check if target is in left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1  # Search right
            else:  # Right side is sorted
                # Check if target is in right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search right
                else:
                    right = mid - 1  # Search left
        
        return -1