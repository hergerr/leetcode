class Solution:
    def myAtoi(self, s: str) -> int:
        signs = ['+','-']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        whitelist = signs + numbers
        # absolute value for minimun
        MIN = 2**31
        MAX = 2**31 - 1
        s = s.lstrip()
        result = 0
        if not s:
          return result

        # first position can be +, - or invalid
        if s[0] not in whitelist:
            return result
        if s[0] == "+":
          s = s[1:]
          is_positive = True
        elif s[0] in numbers:
          is_positive = True
        elif s[0] == "-":
            s = s[1:]
            is_positive = False
        
        for char in s:
          if char not in numbers:
            if not is_positive:
              result *= -1
            return result
          result = result * 10 + int(char)

          if is_positive and result > MAX:
              return MAX
          if not is_positive and result > MIN:
              return MIN * -1
        
        if not is_positive:
            result *= -1

        return result

x = Solution()
result = x.myAtoi("")
print(result)