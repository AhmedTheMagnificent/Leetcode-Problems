class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ""
        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                string += chr(ord(s[i]) + 32)
            else:
                string += s[i]
        return string

