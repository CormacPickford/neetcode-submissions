class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        uniqs = {s[0]}
        l=0
        best_length = 1
        temp_length = 1
        for r in range(1,len(s)):
            while s[r] in uniqs:
                uniqs.discard(s[l])
                l+=1
                temp_length-=1
            uniqs.add(s[r])
            r+=1
            temp_length+=1
            best_length = max(best_length,temp_length)
        return best_length



        
        