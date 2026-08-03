class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        tta = []
        for i in range(len(speed)):
            tta.append((target-position[i])/float(speed[i]))
        
        ma = defaultdict(int)
        for i in range(len(position)):
            ma[position[i]] = tta[i]
        position = sorted(position)
        r = len(position) -1
        res = 1
        for i in range(len(position)-1,-1,-1):
                if ma[position[i]] > ma[position[r]]:
                    res+=1
                    r = i
        return res


        
        
