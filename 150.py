from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    operators = ['+', '-', '*', '/']
    stack = []
    for item in tokens:
      if item in operators:
        elem_1 = stack.pop()
        elem_2 = stack.pop()
        if item == "+":
          result = elem_2 + elem_1
        elif item == "-":
          result = elem_2 - elem_1
        elif item == "*":
          result = elem_2 * elem_1
        elif item == "/":
          result = int(elem_2 / elem_1)
        stack.append(result)
      else:
        number = int(item)
        stack.append(number)
    return stack.pop()


solution = Solution()
result = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(result)
