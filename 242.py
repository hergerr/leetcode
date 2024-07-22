class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.fill_dict(s)
        dict_t = self.fill_dict(t)

        return dict_s == dict_t

    def fill_dict(self, word):
        counter_dict = {}
        for char in word:
            if char in counter_dict:
                counter_dict[char] += 1
            else:
                counter_dict[char] = 1
        return counter_dict
