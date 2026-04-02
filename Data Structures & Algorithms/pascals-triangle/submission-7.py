class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rows_num in range(numRows):
            row = [1]*(rows_num+1)
            for j in range(1,rows_num):
                row[j]=triangle[rows_num-1][j-1]+triangle[rows_num-1][j]

            triangle.append(row)
        return triangle
        