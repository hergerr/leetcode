from typing import List

class Solution:

  def encode(self, strs: List[str]) -> str:
    output = ''
    for word in strs:
      output += f'{len(word)}#{word}'
    return output

  def decode(self, s: str) -> List[str]:
    if not s:
      return []
    output = []
    word_entity_start = 0
    while True:
      length_string = ''
      length_int = None
      while True:
        char = s[word_entity_start]
        if char == '#':
          length_int = int(length_string)
          break
        else:
          length_string += char
          word_entity_start += 1
      # skip special character
      word_entity_start += 1
      word = slice(word_entity_start, word_entity_start + length_int)
      output.append(s[word])
      word_entity_start += length_int
      if word_entity_start == len(s):
        return output

x = Solution()
y = x.encode(["we","say",":","yes","!@#$%^&*()"])
print(y)
z = x.decode(y)
print(z)