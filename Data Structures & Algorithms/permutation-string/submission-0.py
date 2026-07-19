class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        le = len(s1)
        for l in range(len(s2)):
            sub = s2[l:l+le]
            if sorted(sub) == sorted(s1):
                return True
        return False
        