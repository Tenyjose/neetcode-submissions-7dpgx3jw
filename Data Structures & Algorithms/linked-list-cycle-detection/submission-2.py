"""
PROBLEM UNDERSTANDING

Detect if a linked list has a cycle.

A cycle exists if following next pointers leads back to a 
previously visited node.

Input: Head of linked list
Output: True if cycle exists, False otherwise

Constraints:
- Must be O(1) space (can't use hash set)
- List can be empty or single node

Edge cases: Empty list, no cycle, cycle at various positions
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        APPROACH
        
        Floyd's Cycle Detection (Tortoise and Hare algorithm).
        
        Strategy:
        1. Use two pointers moving at different speeds
        2. Slow pointer moves 1 step at a time
        3. Fast pointer moves 2 steps at a time
        4. If there's a cycle, fast will eventually catch up to slow
        5. If there's no cycle, fast reaches the end (None)
        
        Why this works:
        - If there's a cycle, both pointers enter the cycle
        - Once in cycle, they're running in a loop
        - Fast moves 2x speed, so it catches slow eventually
        - Distance between them decreases by 1 each step
        - They MUST meet (can't skip over each other)
        
        Time Complexity: O(n)
        - If no cycle: Fast reaches end in n/2 steps
        - If cycle: Fast catches slow in at most n steps
        
        Space Complexity: O(1)
        - Only two pointer variables
        """
        
        slow = fast = head
        
        # Fast pointer moves 2 steps, so check both fast and fast.next
        while fast and fast.next:
            # Move pointers
            slow = slow.next       # 1 step
            fast = fast.next.next  # 2 steps
            
            # Check if they met
            if slow == fast:
                return True  # Cycle detected!
        
        # Fast reached end (None), no cycle
        return False

"""
REASONING

Floyd's algorithm uses speed difference to detect cycles.

Example with cycle: 3→2→0→-4→(back to 2)

Step 1: slow=2, fast=0 (both moved from 3)
Step 2: slow=0, fast=2 (fast wrapped around)
Step 3: slow=-4, fast=-4 (they meet!) ✓

Why they can't skip each other:
Once both are in cycle, fast gains 1 position per iteration.
If distance between them is D:
- After 1 step: D-1
- After 2 steps: D-2
- After D steps: 0 (they meet)

Example without cycle: 1→2→3→None

Step 1: slow=2, fast=3
Step 2: slow=3, fast=None (reached end)
Return False ✓

Edge cases:
- Empty list: fast=None, loop doesn't run ✓
- Single node, no cycle: fast.next=None, loop doesn't run ✓
- Two nodes with cycle: They meet after 1-2 iterations ✓

Alternative: Hash set to track visited nodes would be O(n) space.
This solution is optimal with O(1) space.
"""