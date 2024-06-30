class Solution:


    def reverse(self, x: int) -> int:
        is_negative = x < 0
        MAX = 2**31
        result = 0
        
        x = abs(x)
        while x > 0:
          # pop operation
          pop = x % 10
          x = int(x / 10)

          # overflow check
          if is_negative:
            if result > MAX / 10:
              return 0
            if result == MAX / 10 and pop > 8:
              return 0
          else:
            if result > MAX / 10:
                return 0
            if result == MAX / 10 and pop > 7:
                return 0

          # push operation
          temp = result * 10 + pop
          result = temp
        
        if is_negative:
           result *= -1

        return result


x = Solution()
result = x.reverse(210)
print(result)