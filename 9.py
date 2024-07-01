class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        length = len(string)
        for i in range(0, int(length / 2)):
          if string[i] != string[length - i - 1]:
             return False
        return True
    
    def isPalindromeBis(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed = 0
        original = x
        while x:
           mod = x % 10
           x = x // 10
           reversed = reversed * 10 + mod
        return original == reversed
                     

x = Solution()
y = x.isPalindromeBis(-121)
print(y)