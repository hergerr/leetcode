from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # index serves as number of repetitions, value as the number, which occured i-times
    buckets = [[] for _ in range(len(nums) + 1)]
    counter = {}
    result = []
    for element in nums:
      counter[element] = 1 + counter.get(element, 0)
    
    for key, value in counter.items():
      buckets[value].append(key)

    for j in range(len(buckets) - 1, 0, -1):
      for i in buckets[j]:
        result.append(i)
        if len(result) == k:
          return result

x = Solution()
y = x.topKFrequent([-1, -1], 1)
print(y)