from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []
    for index, temperature  in enumerate(temperatures):
      while len(stack) and stack[-1][0] < temperature:
        _ , poped_index = stack.pop()
        result[poped_index] = index - poped_index
      stack.append((temperature, index))
    return result

solution = Solution()
result = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(result)
