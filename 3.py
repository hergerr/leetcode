class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        longest = 0
        sett = set()
        n = len(s)
        # move the right pointer as long as the substring is valid
        for right_pointer in range(n):
            # move the left pointer, when the substring is not valid 
            while (s[right_pointer] in sett):
                sett.remove(s[left_pointer])
                left_pointer += 1

            sett.add(s[right_pointer])
            subst_len = right_pointer - left_pointer + 1
            longest = max(subst_len, longest)

        return longest

x = Solution()
y = x.lengthOfLongestSubstring("vvvvvvv")
print(y)