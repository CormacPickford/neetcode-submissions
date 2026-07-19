class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        b_l,b_r = 0,-1
        l = 0
        countt = [0] * 52
        counts = [0] * 52
        satisfied = 52 - len(set(t))
        mlen = len(s) +1
        for i in t:
            countt[self.getidx(i)] +=1
        for r in range(len(s)):
            counts[self.getidx(s[r])] +=1
            
            if countt[self.getidx(s[r])] == counts[self.getidx(s[r])]:
                satisfied += 1
            while satisfied == 52:
                if r-l+1 < mlen:
                    b_l,b_r = l,r

                    mlen = r-l+1
                counts[self.getidx(s[l])] -=1
                
                if countt[self.getidx(s[l])] == counts[self.getidx(s[l])] + 1:
                    satisfied -= 1
                l +=1
        return s[b_l:b_r+1]











    def getidx(self,cha):
        if ord(cha) > ord('Z'):
            return ord(cha) - ord('a') + 26
        return ord(cha) - ord('A')


