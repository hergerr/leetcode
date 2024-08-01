from  typing import List
# idea: prefix sum for each row
# then - summing the sums over the rows of given rectangle


class NumMatrix:

  def __init__(self, matrix: List[List[int]]):
    self.prefix_matrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
      sum = 0
      for j in range(len(matrix[i])):
        sum += matrix[i][j]
        self.prefix_matrix[i].append(sum)
    

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    # for each row
    sum = 0
    for row in range(row1, row2 + 1):
      # add them to the sum
      if col1 == 0:
        sum += self.prefix_matrix[row][col2]
      else:
        sum += self.prefix_matrix[row][col2] - self.prefix_matrix[row][col1 - 1]
    return sum
  
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(2, 1, 4, 3)) # return 8 (i.e sum of the red rectangle)
print(numMatrix.sumRegion(1, 1, 2, 2)) # return 11 (i.e sum of the green rectangle)
print(numMatrix.sumRegion(1, 2, 2, 4)) # return 12 (i.e sum of the blue rectangle)
