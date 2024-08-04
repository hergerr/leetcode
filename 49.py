from typing import List
from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    results = defaultdict(list)
    
    for string in strs:
      arr = [0] * 26
      
      for char in string:
        index = ord(char) - ord('a')
        arr[index] += 1
      # tuple is immmutable, and can serve as a key
      key = tuple(arr)
      results[key].append(string)
    return results.values()

x = Solution()
y = x.groupAnagrams(["ddddddddddg","dgggggggggg"])
print(y)