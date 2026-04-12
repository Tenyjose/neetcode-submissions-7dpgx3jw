class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c in match_dict.keys():
                stack.append(c)
            else:
                    if not stack:
                        return False
                    top = stack.pop()
                    if match_dict[top]!= c:
                        return False
        return len(stack) == 0
