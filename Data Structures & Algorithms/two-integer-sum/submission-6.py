"""
PROBLEM UNDERSTANDING

Given the array of integers and target value, i have to find the find the 
two numbers in the array that add upto target and return their indices

input:
    - nums: An array of intergers(eg: [2,3,6,8])
    - target : target value(eg: 5)

output:
    - An array of indices(eg: [0,1] -> nums[0]+nums[1] = 2+3 = 5)

constraints:
    - Excatly one solution or each input array
    - The two indices cannot be the same 
    - All input has atleast two integers

Edge cases to consider:
    - target could be negative
    - minimum array legth is 2

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        APPROACH

        I would use a hash map(dictionary) to tarck the numbers that
        I have seen.

        As I Iterate through the array:
         - for current number calculater the difference
         - check if the diff already exist in the hash map:
            - If exist : found the pair.Return both indices
            - if not, add the differenc eto the hash map

        Since I'm using hash map the lookup would be faster.
        Also only a single pass is required

        so, Time Complexity would be O(n)
        and Space complexit would be O(n)        
        """

        # hash map to store the seen differances
        seen = {}

        # loop throught array with both index and value
        for i,num in enumerate (nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i

        # should never reach here based on problem constraint
        return []

"""
REASONING

This works because as i iterate i check if the other half already
exists. Using hash maps give faster lookups time.

EX: nums = [2,3,6,8], target = 5
    i = 0 , num = 2, -> Diff = 3 , not in seen , add to seen -> {2:0}
    i= 1 , num = 3 -> Diff = 2 ,present in seen , So it return [0,1]
"""