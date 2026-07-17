class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sols = []
        print(nums)
        for i,n_1 in enumerate(nums):
            target = -n_1
            l = i+1
            r = len(nums) - 1
            print(n_1)
            print(l)
            print(r)
            while (i <= len(nums) - 2) and (l<r):
                
                if nums[l]+nums[r] < target:
                    l+=1
                elif nums[l]+nums[r] > target:
                    r-=1
                elif nums[l]+nums[r] == target:
                    sols.append([n_1,nums[l],nums[r]])
                    l+=1
        set_sol = [c for i,c in enumerate(sols) if c not in sols[:i]]
        return set_sol


            

        