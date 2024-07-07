class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = s.lower()
        letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        left_pointer = 0
        right_pointer = len(input) - 1
        while left_pointer <= right_pointer:
            if input[left_pointer] not in letters:
                left_pointer += 1
                continue
            if input[right_pointer] not in letters:
                right_pointer -= 1
                continue
            if input[left_pointer] != input[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True

x = Solution()
y = x.isPalindrome("0P")
print(y)