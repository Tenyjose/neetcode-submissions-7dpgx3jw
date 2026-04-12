"""
PROBLEM UNDERSTANDING

Encode list of strings into single string, then decode back.
Must handle any characters including delimiters.

Input: List of strings
Output: Encoded string (or decoded list)

Challenge: Strings can contain any character, so need robust encoding.
Edge cases: Empty strings, strings with '#', multi-digit lengths
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        """
        APPROACH - DECODE
        
        Read length, skip '#', extract that many characters.
        
        Steps:
        1. Find '#' to get length
        2. Extract next 'length' characters
        3. Repeat until done
        
        Time: O(n), Space: O(n)
        """
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i += length
        return res



"""
REASONING

Length-prefix handles edge cases elegantly.

Example: ["hello#world","test"]
→ "11#hello#world4#test"
→ Read "11", extract 11 chars including the '#' inside ✓

Works for:
- Empty: "0#"
- With delimiter: "3#a#b" (3 chars, one is '#')
- Multi-digit: "100#" + 100 chars

Alternative: Escape characters, but length-prefix is cleaner.
"""
