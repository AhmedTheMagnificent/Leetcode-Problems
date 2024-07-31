class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ''
        for i in s:
            if (i >= 'a' and i <= 'z') or (i >= '0' and i <= "9"):
                string += i
        return string == string[::-1]
