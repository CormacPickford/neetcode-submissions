from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        top = [c.most_common(k)[i][0] for i in range(k)]
        return top