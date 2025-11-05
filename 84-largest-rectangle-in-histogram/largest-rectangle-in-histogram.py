# class Solution:
#     def largestRectangleArea(self, heights: list[int]) -> int:
#         #brute force
#         maxarea = 0

#         for i, h in enumerate(heights):
#             rightmost = i
#             while rightmost < len(heights) and heights[rightmost] >= h:
#                 rightmost += 1
#             rightmost -=1

#             leftmost = i
#             while leftmost >= 0 and heights[leftmost] >= h:
#                 leftmost -= 1
#             leftmost += 1 

#             maxarea = max(maxarea, h * (rightmost - leftmost + 1))
        
#         return maxarea


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #monotonically increasing stack
        maxarea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index))
                start = index
            
            stack.append((start,h))
        
        for i,h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        
        return maxarea