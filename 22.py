from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []
    stack = []
    
    def backtrack(opening, closing):
      if opening == closing == n:
        result.append("".join(stack))
        return
      if opening < n:
        stack.append("(")
        backtrack(opening + 1, closing)
        stack.pop()
      if opening > closing:
        stack.append(")")
        backtrack(opening, closing + 1)
        stack.pop()
    backtrack(0, 0)
    return result
  
solution = Solution()
result = solution.generateParenthesis(3)
print(result)
