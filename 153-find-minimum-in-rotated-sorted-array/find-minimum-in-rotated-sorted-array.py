class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("infinity")
        l, r = 0, len(nums) - 1

        while l<=r:
            if nums[l]<nums[r]:
                #Entirely sorted
                res = min(res, nums[l])
            
            mid = (l+r)//2
            #Compare mid for nums
            res = min(res, nums[mid])

            #check for sorted half, traverse to the unsorted
            if nums[mid] >= nums[l]:
                #sorted half
                l = mid + 1
            else:
                #unsorted half as nums[mid]<nums[l]
                r = mid - 1
        
        return res