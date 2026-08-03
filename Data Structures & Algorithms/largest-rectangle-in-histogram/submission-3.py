class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        mstack = []
        rw = [0] * l
        lms = 0
        if l == 1:
            return heights[0]
        if l == 0:
            return 0
        for i,val in enumerate(heights):
            



            while lms > 0 and val < mstack[-1][1]:
                    
                    t_i,t_val = mstack.pop()
                    rw[t_i] = i - t_i
                    lms-=1
            mstack.append([i,val])
            lms+=1

            if i == l-1:
                
                for t_i,t_val in mstack:
                    rw[t_i] = l - t_i


        mstack = []
        lw = [0] * l
        lms = 0
        for i,val in enumerate(heights[::-1]):

            while lms > 0 and val < mstack[-1][1]:
                    t_i,t_val = mstack.pop()
                    lw[l-t_i-1] = i - t_i
                    lms-=1
            mstack.append([i,val])
            lms+=1

            if i == l-1:
                for t_i,t_val in mstack:
                    lw[l-t_i-1] = l - t_i

        tw = []
        res = 0
        print(lw)
        print(rw)
        for i in range(l):
            width  = lw[i] + rw[i] - 1
            arr = width * heights[i]
            res = max(arr,res)
        return res




                



