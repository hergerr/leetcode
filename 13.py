class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_ascending = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M':1000
        }
        sum = 0
        for i in range(len(s)):
            value = symbols_ascending[s[i]]
            if i == len(s) - 1:
                sum += value
                return sum
            
            next_value = symbols_ascending[s[i +1]]
            if value < next_value:
                sum -= value
            else:
                sum += value


x = Solution()
y = x.romanToInt('MCMXCIV')
print(y)