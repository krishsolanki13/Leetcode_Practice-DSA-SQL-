class Solution:
    def findDuplicate(self, nums:list[int]) -> int:
        #Floyds, treat as LL, O(n) for time and O(1) for space, but 
        # no modification of the array. 
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            #Math behind this in notes
            if slow == slow2:
                return slow