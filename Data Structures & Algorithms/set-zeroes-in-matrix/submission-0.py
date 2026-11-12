class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # print(f"{r},{c} = {matrix[r][c]}")
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
    
        # turn rows 1-x into 0
        for r in range(1,len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
        
        # turn columns 1-y into 0
        for c in range(1,len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(1,len(matrix)):
                    matrix[r][c] = 0
        
        # turn the first row and column to 0
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
            for c in range(len(matrix[0])):
                matrix[0][c] = 0