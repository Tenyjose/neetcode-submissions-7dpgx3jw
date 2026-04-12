"""
PROBLEM UNDERSTANDING

Given an array of integers and a target value,
I have to return the indices of two numbers whose sum
add upto the target.

Inputs:
    - An integer array numbers(sorted in non-decreasing order)
    - The target value

Output:
    - The indices of the numbers whose sum add upto target.

Constraints:
    - There will only be one valid solution
    - The space complexity should be O(1)
    - Same element cannont be used twice
    - The returning indices should be 1-indexed(indexes starting from 1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        APPROACH

        SInce the array is sorted in non-decreasing order(ascending order)
        the small lefts would be on the left and bigger ones would be
        on the right.

        So I can use two pointerd and place them at both ends and check
        for conditions

        Once I get the sum of values at both ends, i can use that 
        to narrow down my search. If the curr_sum of first iteration
        is same as the target we return that. But if its less than 
        than target value then its clear that the we have to increase 
        the curr_sum so i increment the left and similarly if the 
        curr_sum is greater than the target that means I have to
        lower the curr_sum to get the target value so I can decremnt 
         from right.

         Time Complexity : O(n)
         Spce complexity : O(1)
        """
        left = 0
        right = len(numbers)-1

        while left < right:
            curr_sum = numbers[left]+numbers[right]
            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1

        # should not be excecuting according to problem statement
        return [-1,-1]

"""
REASONING

This is optimal and requires only the additional space of O(1)
as we are not defining any additional Data staructure.

FOR EXAMPLE:

numbers = [1,,2,3,4]  target = 3

Intialy, Left = 0, Right = 3
        s[Left] = 1, s[Right] =  4
        curr_sum = 1+4 = 5  which is not equal to target and aldo greater than target.
So we decrement the value of Right to bring the curr_sum down.

So,     Left = 0, Right = 2
        s[Left] = 1, s[Right] = 3
        curr_sum = 1+3 = 4 not eual to target and is greater than target
so again we decremnt the value of Right.

Now,    Left = 0, Right = 1
        s[Left] = 1, s[Right] = 2
        curr_sum = 1+2 = 3 , Which equals to the target.
        So we got the requred target as sum
        And return those indices in 1-indexed format.
"""