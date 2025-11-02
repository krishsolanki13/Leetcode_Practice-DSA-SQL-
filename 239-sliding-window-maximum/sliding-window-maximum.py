# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         #Brute Force
        
#         l = 0
#         r = k - 1
#         res = []

#         while r < len(nums):
#             res.append(max(nums[l:r+1]))
#             l+=1
#             r+=1
        
#         return res

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Monotonically decreasing queue

        q = collections.deque()
        l, r = 0, 0
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l+=1
            
            r +=1
    
        return res

