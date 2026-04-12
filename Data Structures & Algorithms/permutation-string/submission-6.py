class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map =defaultdict(int)
        for char in s1:
            s1_map[char] += 1
        
        s2_map = defaultdict(int)
        for i in range(len(s1)):
            s2_map[s2[i]] += 1

        if s1_map == s2_map:
            return True 

        for i in range(len(s1),len(s2)):
            new_char = s2[i]
            s2_map[new_char] += 1

            rmv_char = s2[i-len(s1)]
            s2_map[rmv_char] -= 1

            if s2_map[rmv_char] == 0:
                del s2_map[rmv_char]

            if s2_map == s1_map:
                return True

        return False

