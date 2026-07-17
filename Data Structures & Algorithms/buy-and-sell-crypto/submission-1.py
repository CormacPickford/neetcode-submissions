class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        minscan = [prices[0]]
        for i in range(1,len(prices)-1):
            minscan.append(min(minscan[-1],prices[i]))
        maxscan = [prices[-1]]
        for j in range(-2,-len(prices),-1):
            maxscan.append(max(maxscan[-1],prices[j]))
        print(minscan)
        print(maxscan)
        maxscan = maxscan[::-1]
        diffs = [maxscan[i] - minscan[i] for i in range(len(prices)-1)]
        ma = max(diffs)
        return max(0,ma)

        


