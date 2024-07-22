from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for number in nums:
            if number in elements:
                elements[number] += 1
                if elements[number] == 2:
                    return True
            else:
                elements[number] = 1
        return False

