def isBadVersion(version: int) -> bool:
  return version == 4


class Solution:
  def firstBadVersion(self, n: int) -> int:
    low = 1
    high = n
        
    while low <= high:
      mid = (low + high) // 2
      is_bad = isBadVersion(mid)
      if is_bad:
        if not isBadVersion(mid - 1):
          return mid
        high = mid - 1
      else:
        low = mid + 1

solution = Solution()
result = solution.firstBadVersion(5)
print(result)
