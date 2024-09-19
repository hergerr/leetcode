from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    left_pointer = 0
    m = len(matrix)
    n = len(matrix[0])
    right_pointer = m * n - 1
    
    while left_pointer <= right_pointer:
      print(left_pointer, right_pointer)
      mid = (left_pointer + right_pointer) // 2
      mid_value = matrix[mid // n][mid % n]
      if mid_value > target:
        right_pointer = mid - 1
      elif mid_value < target:
        left_pointer = mid + 1
      else:
        return True
    return False

solution = Solution()
result = solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(result)
