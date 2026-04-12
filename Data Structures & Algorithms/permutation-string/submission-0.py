class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        target = {}
        for char in s1:
            target[char] = target.get(char,0)+1
        
        window = {}
        for i in range(len(s1)):
            char = s2[i]
            window[char] = window.get(char,0)+1
        if target == window:
            return True
        
        for i in range(len(s1),len(s2)):
            add_char = s2[i]
            window[add_char] = window.get(add_char,0)+1

            rmv_char = s2[i-len(s1)]
            window[rmv_char] -= 1

            if window[rmv_char] == 0:
                del window[rmv_char]

            if window ==  target:
                return True

        return False