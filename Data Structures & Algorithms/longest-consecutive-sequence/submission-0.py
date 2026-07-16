class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = (set(nums))
        chains = []
        fps = set()
        for i in nums:
            if not i-1 in s_nums:
                chains.append([i])
        for chain in chains:
            while (chain[-1] + 1) in s_nums:
                chain.append(chain[-1] +1 )
        mlen = 0
        for chain in chains:
            mlen = max(mlen,len(chain))
        return mlen




        

        

        
        
            

        
    