"""
PROBLEM UNDERSTANDING

Given an array of numbers  and value k I have to find out the
k most frequent elemnts in each input array.

input : 
    - a integer array nums
    - value k, which is the number of frequent elements to me returned

output : 
    - an array with k frequent integers

constraints:
    - there is only a unique answer
    - order of result dosent matter
    - nums will always have an integer or more
    - k value would be greater than or equal to 1
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        APPROACH

        Since i have to maintain a count of each integer I have to use a
        Hash map for that.

        Then once i get the count i can use that count to group the 
        integers based on there count.

        Once grouped i can itreate from the end and once it meets
        the condition , i can return the list.

        Time Complexity : O(n)
        Space complexity : O(n)
        """
        
        count = {}
        freq = [[] for _ in range (len(nums)+1)]

        for num in nums:
            count[num] = count.get(num,0)+1
        for num,cnt in count.items():
            freq[cnt].append(num)

        # will hold the array to be returned
        res = []
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

"""
REASONING

Once i get the count of eaach integer in the array, I used that to 
create a list of where each element is stored at an index value
which is its count basically.

Since each list holds values that are of similar counts.. I can iterate 
through the loops till the condition is meet (len(res) == k) and then
return the res list
"""