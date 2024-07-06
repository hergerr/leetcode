from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer <= right_pointer:
            left_value = s[left_pointer]
            right_value = s[right_pointer]
            s[left_pointer] = right_value
            s[right_pointer] = left_value
            left_pointer += 1
            right_pointer -= 1
        return s


x = Solution()
y = x.reverseString(["h","e","l","l","o"])
print(y)