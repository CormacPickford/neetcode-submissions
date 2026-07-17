class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        if len(s) <=k:
            return k
        l = 0
        r = k+1
        for char in s[:k+1]:
            count[char] +=1
        width = k + max(count.values())
        best_width = width
        while r < len(s):
            count[s[r]] +=1
            width = k + max(count.values())
            print(width)
            print(count)
            while r-l+1 > width:
                count[s[l]] -=1
                l+=1
            r+=1
            best_width = max(best_width,width)
        return min(best_width,len(s))

