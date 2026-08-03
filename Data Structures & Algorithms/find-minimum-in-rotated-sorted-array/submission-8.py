class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)-1
        while l < r:
            m = int((l+r)/2)
            print(m)
            print(l)
            print(r)
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] < nums[l]:
                r = m
            else:
                l = max(m,l+1)
            
            
        return min(nums[0],nums[-1])
            
            

        