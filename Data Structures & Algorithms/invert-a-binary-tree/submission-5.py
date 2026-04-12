"""
PROBLEM UNDERSTANDING

Invert a binary tree (mirror it).

Input: Root of binary tree
Output: Root of inverted tree

Invert means: swap left and right children at EVERY node.

Example:
Input:     4           Output:     4
          / \                     / \
         2   7                   7   2
        / \ / \                 / \ / \
       1  3 6  9               9  6 3  1

Edge cases: Empty tree, single node, already inverted
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        APPROACH
        
        Recursive solution - swap children at each node.
        
        Strategy:
        1. Base case: if node is None, return None
        2. Swap left and right children
        3. Recursively invert left subtree
        4. Recursively invert right subtree
        5. Return the root
        
        Why recursion works:
        Inverting a tree = swap children + invert each subtree
        This naturally fits recursive structure.
        
        Each recursive call handles one subtree.
        Base case (None) stops recursion at leaves.
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack depth
          h = tree height
          Balanced tree: O(log n)
          Worst case: O(n)
        """
        
        # Base case: empty tree
        if not root:
            return None
        
        # Swap left and right children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # Alternative Python way:
        # root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return inverted tree
        return root

"""
REASONING

Recursion naturally handles tree structure.

Example trace: invertTree(4) where tree is:
       4
      / \
     2   7

Step 1: Swap at root
  4's children: 2, 7 → swap → 7, 2
  
Step 2: Recurse on left (now 7)
  invertTree(7) swaps its children
  
Step 3: Recurse on right (now 2)
  invertTree(2) swaps its children
  
Result: Fully inverted tree ✓

Base case crucial:
- Prevents infinite recursion
- Handles leaf nodes (children are None)
- Handles empty tree input

Why swap before recursing:
Order doesn't matter much here, but swapping first
means we invert current node, then handle subtrees.

Alternative: Iterative with queue (BFS) also works
but recursion is cleaner and more intuitive.
"""
