class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums) > 0:
            i = nums.pop()
            if i in nums:
                return  True
        return False
            
                

        