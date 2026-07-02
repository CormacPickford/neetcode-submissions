class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in range(len(nums)):
            if nums[i] ==0:
                temp = nums.copy()
                temp.pop(i)
                prod_2 = 1
                for j in temp:
                    prod_2 *= j
                out = [0] * (len(nums))
                out[i] = prod_2
                return out
            prod*=nums[i]


        
        out = [prod] * len(nums)
        for i in range(len(nums)):
            
            out[i] = out[i] // nums[i]
        return out
        