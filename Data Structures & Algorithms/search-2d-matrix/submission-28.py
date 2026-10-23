class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #getRow
 
        ROWS = len(matrix)  -1
        COLS = len(matrix[0]) -1
        l = 0 
        r = len(matrix)-1
        rowFound = 0
        print("ROWS", ROWS)
        print("COLS", COLS)
        while l<=r:
            m = (l+r)//2
            print(m,"m")
            if 0 <= m <= ROWS:
                # print("[m]==>",m)
                # print("matrix[m]",matrix[m])
                # print("matrix[m][0]",matrix[m][0])
            
                # print("matrix[m][COLS]]",matrix[m][COLS])
                if target >= matrix[m][0] and target <= matrix[m][COLS]:
                    print("row found")
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
            print("COL M", m)
            print("rowFound" , rowFound)
            print( 0 <= m <= COLS)
            if 0 <= m <= COLS:
               
                if target == matrix[rowFound][m]:
                    return True
                elif target > matrix[rowFound][m]:
                    print("in here ?")
                    l=m+1
                    print('l', l , 'r', r)
                elif target < matrix[rowFound][m]:
                    r=m -1
            else:
                break

        return False


        
