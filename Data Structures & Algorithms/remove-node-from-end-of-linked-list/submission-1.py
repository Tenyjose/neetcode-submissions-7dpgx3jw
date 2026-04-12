"""
PROBLEM UNDERSTANDING

Remove the nth node from the end of a linked list.

Input: 
- head: head of linked list
- n: position from end (1-indexed)

Output: Head of modified list

Example:
Input: 1→2→3→4→5, n=2
Output: 1→2→3→5 (removed 4)

Constraints:
- List length >= 1
- 1 <= n <= length
- Must do in one pass

Edge cases: Remove head, single node, remove last
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        APPROACH
        
        Two-pointer technique with n-node gap.
        
        Strategy:
        1. Create dummy node (handles removing head)
        2. Use two pointers: p1 and p2
        3. Move p2 forward while counting
        4. Once count > n, start moving p1 too
        5. This maintains gap of n nodes between them
        6. When p2 reaches end, p1 is before target node
        7. Delete p1.next
        
        Why dummy node:
        If we need to remove head (nth from end = length),
        we need a node before head to delete it.
        Dummy provides this.
        
        Why this works:
        By maintaining n-node gap, when p2 hits end,
        p1 is exactly at the node BEFORE the one to delete.
        
        Time Complexity: O(L) - single pass
        Space Complexity: O(1) - only pointers
        """
        
        # Dummy node to handle edge case of removing head
        dummy = ListNode(0, head)
        p1 = dummy
        p2 = head
        count = 0
        
        # Move p2 and count nodes
        # Start moving p1 once gap of n is established
        while p2 != None:
            p2 = p2.next
            count += 1
            
            # Once we've moved n nodes, start moving p1
            if count > n:
                p1 = p1.next
        
        # p1 is now before the node to delete
        # Remove p1.next
        p1.next = p1.next.next
        
        # Return actual head (skip dummy)
        return dummy.next

"""
REASONING

Two-pointer technique maintains n-node gap for precise positioning.

Example: head=1→2→3→4→5, n=2

Setup: dummy→1→2→3→4→5

Move p2, establish gap:
- p2 at 2, count=1, gap not established
- p2 at 3, count=2, gap not established
- p2 at 4, count=3, gap established! Move p1 to 1
- p2 at 5, count=4, move p1 to 2
- p2 at None, count=5, move p1 to 3

Now: p1 at 3, p2 at None
p1.next (node 4) is the target!
p1.next = p1.next.next (node 5)

Result: 1→2→3→5 ✓

Why count > n (not count >= n):
We want p1 to be BEFORE the target node.
If count > n, we've created the right gap.

Edge case - Remove head:
head=1→2, n=2
p2 moves to None, count=2
count > 2? NO, p1 stays at dummy
p1.next = dummy.next.next
Result: 2 ✓ (removed head)

Alternative: Two-pass (count length, then remove) uses same time
but requires two traversals. One-pass is more elegant.
"""