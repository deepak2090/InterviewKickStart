class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromecheck(i,j):
            left = i
            right = j-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            return True
        for i in range(len(s)):
            for j in range(len(s),0,-1):
                if palindromecheck(i,j):
                    return s[i:j] #leftpointerrightpointer
                    