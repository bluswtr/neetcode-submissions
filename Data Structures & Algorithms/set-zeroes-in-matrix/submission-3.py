class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix) # rows
        cols = len(matrix[0]) # cols
        trackRow = [1] * rows
        trackCol = [1] * cols

        # matrix[r,c]
        # mark up
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    trackCol[c] = 0
                    trackRow[r] = 0

        # fill matrix
        for r in range(rows):
            for c in range(cols):
                if trackCol[c] == 0 or trackRow[r] == 0:
                    matrix[r][c] = 0
