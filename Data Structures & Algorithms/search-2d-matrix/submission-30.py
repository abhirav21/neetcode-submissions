class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

 
        ROWS = len(matrix)  -1
        COLS = len(matrix[0]) -1
        l = 0 
        r = len(matrix)-1
        rowFound = 0
        while l<=r:
            m = (l+r)//2
            print(m,"m")
            if 0 <= m <= ROWS:

                if target >= matrix[m][0] and target <= matrix[m][COLS]:
                   
                    rowFound = m
                    break
                elif target <= matrix[m][0]:
                    r=m -1
                elif target >= matrix[m][COLS]:
                    l=m+1
            else:
                break
        
        l = 0 
        r = len(matrix[0])-1
        print("rr", r)
        while l<=r:
            m = (l+r)//2

            if 0 <= m <= COLS:
               
                if target == matrix[rowFound][m]:
                    return True
                elif target > matrix[rowFound][m]:
                   
                    l=m+1
                   
                elif target < matrix[rowFound][m]:
                    r=m -1
            else:
                break

        return False


        
