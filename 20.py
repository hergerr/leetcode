class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    braces = {'}': '{', ')': '(', ']': '['}
    for char in s:
      if char in braces.values():
        stack.append(char)
      elif char in braces.keys():
        # too many closing braces
        if stack:
          last_brace = stack.pop()
        else:
          return False
        # order is correct
        if braces[char] == last_brace:
          continue
        else:
          return False
    # something is still left
    if stack:
      return False
    return True

solution = Solution()
result = solution.isValid("({[]})")
print(result)