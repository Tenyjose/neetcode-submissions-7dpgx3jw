class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in grp_anagrams:
                grp_anagrams[key] = []
            grp_anagrams[key].append(word)

        return list(grp_anagrams.values())