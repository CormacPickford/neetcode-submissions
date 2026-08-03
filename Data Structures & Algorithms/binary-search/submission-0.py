class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        l,r = 0,len(nums)
        
        found = -1
        while found == -1 and l!=r:
            cnd = int((r+l)/2)
            if nums[cnd] == target:
                return cnd
            elif nums[cnd] < target:
                l = cnd+1
            else:
                r = cnd
        return found
            

