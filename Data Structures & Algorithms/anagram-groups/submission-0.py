class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        running_list = []
        for i in range(len(strs)):
            fitted = False
            for j in range(len(running_list)):
                if sorted(strs[i]) == sorted(running_list[j][0]):
                    running_list[j].append(strs[i])
                    fitted = True
            if not fitted:
                running_list.append([strs[i]])
        return running_list


                