class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0,0]
        dp = [[False for _ in range(n)] for _ in range(n)]
            
        # initialize
        for i in range(n):
            dp[i][i] = True
            ans = [i, i]
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
        
        diff = 2
        while diff <= n:
            for i in range(0, n - diff):
                j = i + diff
                if (dp[i + 1][j - 1] and s[i] == s[j]):
                    dp[i][j] = True
                    ans = [i, j]
            diff += 1
        
        return s[ans[0]: ans[1]+1]

        
