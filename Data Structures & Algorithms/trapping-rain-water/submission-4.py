class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        tot = 0
        if sum(height) == 0:
            return 0
        if len(height) == 1:
            return 0
        while height[l] == 0:
            l+=1
        buffer = 0
        
        for r in range(l+1,len(height)):
            if height[r] >= height[l]:
                alt = height[l]
                ran = height[l:r]
                water = [alt - r for r in ran]
                tot += sum(water)
                l = r
        tail = height[l:r+1]
        final = tail[::-1]
        print(final)
        l = 0
        for r in range(l+1,len(final)):
            if final[r] >= final[l]:
                alt = final[l]
                ran = final[l:r]
                water = [alt - r for r in ran]
                tot += sum(water)
                l = r
        
        return tot


            
            



        

    
    
   
