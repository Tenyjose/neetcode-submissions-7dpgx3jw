class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        stack = [intervals[0]]

        for start,end in intervals[1:]:
            last_start = stack[-1][0]
            last_end = stack[-1][1]
            if last_end >= start:
                stack[-1][1] = max(end,last_end)

            else:
                stack.append([start,end])

        return stack