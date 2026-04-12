"""
PROBLEM UNDERSTANDING

Merge two sorted linked lists into one sorted list.

Input: Two sorted linked lists (ascending order)
Output: One merged sorted linked list

Example:
list1 = 1 → 2 → 4
list2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4

Edge cases: Empty lists, different lengths, duplicate values
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        APPROACH
        
        Use dummy node and two pointers to merge.
        
        Strategy:
        1. Create dummy node to simplify edge cases
        2. Compare current nodes from both lists
        3. Attach smaller node to result
        4. Move that list's pointer forward
        5. After one list exhausted, attach remainder
        
        Dummy node trick:
        Instead of special-casing the first node, use a dummy
        node at the start. This makes code cleaner.
        
        Time Complexity: O(n + m) where n, m are list lengths
        - Visit each node exactly once
        
        Space Complexity: O(1)
        - Only creating pointers, not new nodes
        - Reusing existing nodes from input lists
        """
        
        # Dummy node to simplify code
        dummy = ListNode(0)
        curr = dummy
        
        # While both lists have nodes to compare
        while list1 and list2:
            # Compare and choose smaller value
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            # Move current pointer forward
            curr = curr.next
        
        # Attach remaining nodes (at most one list has remaining)
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        # Return merged list (skip dummy node)
        return dummy.next

"""
REASONING

Dummy node simplifies merging without special cases.

Example: list1=[1,2,4], list2=[1,3,4]

Initial: dummy → ?, curr=dummy

Step 1: Compare 1 vs 1, pick list1's 1
  dummy → 1
  list1 now at 2, curr at node 1

Step 2: Compare 2 vs 1, pick list2's 1
  dummy → 1 → 1
  list2 now at 3, curr at second node 1

Step 3: Compare 2 vs 3, pick 2
  dummy → 1 → 1 → 2
  list1 now at 4, curr at node 2

Step 4: Compare 4 vs 3, pick 3
  dummy → 1 → 1 → 2 → 3
  list2 now at 4, curr at node 3

Step 5: Compare 4 vs 4, pick list1's 4
  dummy → 1 → 1 → 2 → 3 → 4
  list1 now at None, curr at node 4

Step 6: list1 is None, attach rest of list2
  dummy → 1 → 1 → 2 → 3 → 4 → 4

Return dummy.next ✓

Why while list1 and list2 (not or):
Using 'or' would continue when one is None, causing
AttributeError when trying to access .val on None.

Why attach remaining:
When one list ends, the other is already sorted,
so we can attach all remaining nodes at once.
No need to process them one by one.

Edge cases:
- Empty lists: Loop never runs, attach the non-empty one ✓
- Equal values: Use <= to handle consistently ✓
"""