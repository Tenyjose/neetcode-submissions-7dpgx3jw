"""
PROBLEM UNDERSTANDING

Given a string, find the length of the longest substring
without repeating characters.

Input: String s
Output: Integer (length of longest substring with all unique chars)

A substring is a contiguous sequence of characters.

Constraints:
- String can be empty
- Only need length, not the substring itself
- Characters can be any ASCII

Edge cases: Empty string, single char, all unique, all same
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        APPROACH
        
        Use sliding window technique with a set to track unique characters.
        
        Strategy:
        1. Maintain a window [l, r] with all unique characters
        2. Expand window by moving right pointer
        3. If duplicate found, shrink from left until duplicate removed
        4. Track maximum window size seen
        
        The set ensures O(1) lookup for duplicate checking.
        
        Window invariant: All characters in window are unique.
        
        When duplicate found:
        - Shrink window from left until duplicate is removed
        - This maintains the invariant
        
        Time Complexity: O(n)
        - Each character added to set once: O(n)
        - Each character removed from set once: O(n)
        - Total: O(2n) = O(n)
        
        Space Complexity: O(min(n, m))
        - m = charset size (26 for lowercase, 128 for ASCII)
        - Set contains at most min(n, m) characters
        """
        
        charset = set()  # Tracks characters in current window
        l = 0  # Left pointer (window start)
        res = 0  # Maximum length found
        
        # Right pointer expands the window
        for r in range(len(s)):
            # If duplicate found, shrink window from left
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            # Add current character to window
            charset.add(s[r])
            
            # Update maximum length
            # Window size = r - l + 1
            res = max(res, r - l + 1)
        
        return res

"""
REASONING

Sliding window maintains substring with unique characters.

Example: s = "abcabcbb"

Window expands: [a], [ab], [abc] → length 3
Hit duplicate 'a': shrink to [bca]
Hit duplicate 'b': shrink to [cab]
Hit duplicate 'c': shrink to [abc]
...continues...

Maximum window: 3 ("abc", "bca", or "cab") ✓

Why O(n) not O(n²):
Although there's a while loop inside for loop, each character
is visited at most twice:
- Once when added by right pointer
- Once when removed by left pointer
Total: 2n operations = O(n)

Alternative: Check all substrings would be O(n³), rejected.
Using hash map with last seen index would also work (O(n) time),
but set approach is simpler.
"""