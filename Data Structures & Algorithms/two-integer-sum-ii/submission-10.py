class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_nums = set(numbers)
        if target % 2 == 0 and target/2 in s_nums:
            c = numbers.copy()
            t = c.index(target/2)
            c.remove(target/2)
            print(c)
            if target/2 in c:
                print('here')
                return [t+1,c.index(target/2)+2]
        for n in s_nums:
            if n != target/2:
                if target - n in s_nums:
                    print(n)
                    return sorted([numbers.index(n)+1,numbers.index(target-n)+1])

        