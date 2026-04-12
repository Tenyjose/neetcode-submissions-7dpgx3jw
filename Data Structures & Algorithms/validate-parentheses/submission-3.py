class Solution:
    def isValid(self, s: str) -> bool:
        para_map = {"{":"}","(":")","[":"]"}
        res = []

        for char in s:
            if char in para_map.keys():
                res.append(char)

            elif char in para_map.values():
                if not res:
                    return False
                top = res.pop()
                if para_map[top] != char:
                    return False
        return True if not res else False  

