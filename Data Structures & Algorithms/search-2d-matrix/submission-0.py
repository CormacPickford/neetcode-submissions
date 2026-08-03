class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = matrix[0]
        for i in range(1,len(matrix)):
            arr.extend(matrix[i])
        
        l,r = 0,len(arr)
        while l!=r:
            m = int((l+r)/2)
            if arr[m] == target:
                return True
            if arr[m] > target:
                r = m
            else:
                l = m+1
        return False


        



        