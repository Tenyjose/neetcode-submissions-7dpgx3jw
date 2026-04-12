class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            h1 = -heapq.heappop(heap)  # largest
            h2 = -heapq.heappop(heap)  # second largest

            if h1 == h2:
                continue
            elif h1 > h2:
                heapq.heappush(heap, -(h1 - h2))  # push back as negative!
            else:
                heapq.heappush(heap, -(h2 - h1))  # push back as negative!

        return -heap[0] if heap else 0