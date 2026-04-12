"""
PROBLEM UNDERSTANDING

Gvien a string, I have to check whether the given string is 
palindrome or not.

If it is i have to return true alse false

Input : A string 'S'

Output : A boolean value (T/F)

Constraints: 
    - Case in-sensitive(Eg : A and a are identical/treated equal)
    - Ignore non-alphanumeric characters
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        APPROACH

        A string is a palindrome if it's same from left to right
        and from right to left.

        So a two pointer approach would work. So i can intially place
        two pointers at both ends and check for the conditions.

        I need a left and right pointer. And start checking from both
        ends. When  encounter non-alphanumeric characters, i will
        ingore them and continue to the next.

        whenever the left and right and left pointers become not equal
        we exit an return False.

        If it successfully completes excecution, then the string would be
        a palindrome and It will return True

        Time COmplexity : O(n)
        Space Complexity : O(1)
        """
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            # I use lower fuction to make it case in-sensitive
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1

        return True

"""
REASONING

It works becausewe are checking for non alpha numeric characters with 
two pointer at both ends of string , closing down by comparing 
each character at correcponding step at each step.

FOR EX:

s="teb a cat"

intially s[left] = t , s[right] = t
            no issues, Increment left & right
        s[left] = a , s[right] = a
            no issues, Increment left & right
        s[left] = b , s[right] = c
            They are different.
            The last if staement gets excecuted and False will be returened
            Thus the string is not palindrome.
"""