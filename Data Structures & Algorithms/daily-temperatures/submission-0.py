class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tstack = []
        out = [0] * len(temperatures)
        slen = 0
        istack = []
        for (i,temp) in enumerate(temperatures):
            
            while slen > 0 and temp > tstack[-1]:
                print(tstack)
                out[istack[-1]] = i - istack[-1]
                 
                tstack.pop()
                istack.pop()
                slen -=1
                
            tstack.append(temp)
            istack.append(i)
            
            slen +=1
        return out




