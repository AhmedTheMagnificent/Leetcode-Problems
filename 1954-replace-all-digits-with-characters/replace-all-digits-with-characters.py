class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, num):
            return chr(ord(char) + num)
        string = ""
        for i in range(len(s)):
            if i % 2 == 1:
                string += shift(s[i - 1], int(s[i]))
            else:
                string += s[i]
        return string