"""
PROBLEM UNDERSTANDING

Reorder linked list: L0→L1→...→Ln-1→Ln
Into: L0→Ln→L1→Ln-1→L2→Ln-2→...

Example:
Input: 1→2→3→4→5
Output: 1→5→2→4→3

Approach:
1. Find middle (fast/slow pointers)
2. Reverse second half
3. Merge alternating nodes

Time: O(n), Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        APPROACH
        
        Three-step process:
        1. Find middle using fast/slow pointers
        2. Reverse second half
        3. Merge two halves alternating
        
        Time: O(n) - three passes
        Space: O(1) - only pointers
        """
        
        # Step 1: Find middle
        slow = middle = head
        fast = end = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Step 2: Split and reverse second half
        part2 = slow.next
        slow.next = None  # Split the list
        
        # Reverse part2
        prev = None
        while part2:
            part2next = part2.next
            part2.next = prev
            prev = part2
            part2 = part2next
        
        # Step 3: Merge alternating
        part1, part2 = head, prev
        
        while part2:
            # Save next nodes
            part1next = part1.next
            part2next = part2.next
            
            # Connect alternating
            part1.next = part2
            part2.next = part1next
            
            # Move to next pair
            part1 = part1next
            part2 = part2next

"""
REASONING

Example: 1→2→3→4→5

Step 1 - Find middle:
slow ends at 3

Step 2 - Split and reverse:
part1: 1→2→3
part2: 5→4 (reversed from 4→5)

Step 3 - Merge:
Iteration 1:
  part1=1, part2=5
  Connect: 1→5→2
  Move to: part1=2, part2=4

Iteration 2:
  part1=2, part2=4
  Connect: 1→5→2→4→3
  Move to: part1=3, part2=None

Exit loop (part2 is None)
Result: 1→5→2→4→3 ✓
"""