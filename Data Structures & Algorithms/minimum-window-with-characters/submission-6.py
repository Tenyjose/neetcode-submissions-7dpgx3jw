class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        target = {}
        for char in t:
            target[char] = target.get(char,0)+1

        need = len(target)
        have = 0

        window = {}
        left = 0
        res = ""
        res_len = float('infinity')

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0)+1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                current_len = right - left +1
                if current_len < res_len:
                    res_len = current_len
                    res = s[left:right+1]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                left += 1

        return res

