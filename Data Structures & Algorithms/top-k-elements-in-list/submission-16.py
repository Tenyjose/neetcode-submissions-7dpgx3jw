class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return 0

        freq = [[] for _ in range(len(nums)+1)]
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1

        for num,cnt in hash_map.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res