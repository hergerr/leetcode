def guess(num):
  if num > 6:
    return -1
  elif num < 6:
    return 1
  else:
    return 0

class Solution:
  def guessNumber(self, n: int) -> int:
    low = 1
    high = n
    
    while low <= high:
      mid = (low + high) // 2
      result = guess(mid)
      if result == 1:
        low = mid + 1
      elif result == -1:
        high = mid - 1
      else:
        return mid


solution = Solution()
result = solution.guessNumber(10)
print(result)
