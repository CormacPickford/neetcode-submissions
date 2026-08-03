class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            if len(piles) == 1 and h >= piles[0]:
                return 1
            
            l,r = 0,max(piles)+1
            while l != r:
                m = int((l+r)/2)
                t = 0
                for i in piles:
                    t += (i + m - 1) // m
                if t > h:
                    l = m + 1
                elif t <= h:
                    p = m - 1
                    t = 0
                    for i in piles:
                        t += (i + p - 1) // p
                    if t > h:
                        return m
                    else:
                        r = m
                    


                    



        