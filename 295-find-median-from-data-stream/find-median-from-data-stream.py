class MedianFinder:

    def __init__(self):
       self.left, self.right = [], [] 
       # left -> Max Heap
       # right -> Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # Check whether largest from left is smaller than smallest from right
        if self.left and self.right and ((-1 * self.left[0]) > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        # Check whether the length diff is not more than 1
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right)) 

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return (-1 * self.left[0])
        else:
            return (((-1 * self.left[0]) + self.right[0]) / 2)