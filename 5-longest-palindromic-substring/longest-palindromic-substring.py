class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        def expandAroundCenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
            
        for i in range(n):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        return s[start : end + 1]