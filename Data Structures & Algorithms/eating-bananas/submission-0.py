class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the smallest possible speed for koko is 
        # 1 per/hr and fastest would be the max value in the pile
        # bcoz if she ate at that rate shae would be able ot finish all the 
        # bananas in that period of time.
        left = 1
        right = max(piles)

        while left<=right:
            k = (left+right)//2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            if hours <= h:
                right = k - 1
            else:
                left = k + 1

        return left
