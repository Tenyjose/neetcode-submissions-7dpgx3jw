"""
PROBLEM UNDERSTANDING

Check if two binary trees are identical.

Two trees are identical if:
1. Same structure (nodes in same positions)
2. Same values at corresponding nodes

Example 1 - Same:
p:    1       q:    1
     / \           / \
    2   3         2   3
→ True

Example 2 - Different values:
p:    1       q:    1
     / \           / \
    2   1         2   3
→ False

Example 3 - Different structure:
p:    1       q:    1
     /             \
    2               2
→ False

Edge cases: Both empty, one empty, single nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        APPROACH
        
        Recursive comparison of trees.
        
        Strategy:
        1. If both None → trees are same
        2. If one None, one not → trees different
        3. If values different → trees different
        4. Otherwise → recursively check left AND right subtrees
        
        Base cases:
        - Both None: identical empty trees
        - One None: different structure
        - Different values: different content
        
        Recursive case:
        Trees are same if:
        - Root values match AND
        - Left subtrees match AND
        - Right subtrees match
        
        Why this works:
        Two trees identical = roots match + subtrees identical
        Recursion naturally checks all nodes.
        
        Time Complexity: O(min(n, m))
        - n, m = number of nodes in p, q
        - Visit each node until mismatch found
        - Worst: check all nodes
        
        Space Complexity: O(min(h1, h2))
        - h1, h2 = heights of p, q
        - Recursion stack depth
        - Balanced: O(log n)
        - Worst: O(n)
        """
        
        # Base case 1: Both empty trees
        if not p and not q:
            return True
        
        # Base case 2: One empty, or values different
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive case: Check both subtrees
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

"""
REASONING

Recursion checks trees node by node.

Example: Same trees
p:    1       q:    1
     / \           / \
    2   3         2   3

isSameTree(1, 1):
  Both not None, values match (1 == 1)
  
  Check left: isSameTree(2, 2)
    Both not None, values match
    Check children: isSameTree(None, None) = True
    Return True
  
  Check right: isSameTree(3, 3)
    Same as left
    Return True
  
  Return True AND True = True ✓

Example: Different structure
p:    1       q:    1
     /             \
    2               2

isSameTree(1, 1):
  Values match
  
  Check left: isSameTree(2, None)
    One is None, one isn't
    Return False ✗
  
  Return False AND ... = False ✓

The order of checks matters:
1. Both None first (base case)
2. Then structure/value mismatch
3. Finally recursive calls

This prevents accessing .val on None nodes.

Alternative: Iterative BFS/DFS also works
but recursion is cleaner for tree comparison.
"""