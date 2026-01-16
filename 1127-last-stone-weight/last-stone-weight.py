class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        maxheap = [-x for x in heap]

        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            a, b = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
            
            if a > b:
                heapq.heappush(maxheap, -(a-b))
            
        return -maxheap[0] if maxheap else 0
    

