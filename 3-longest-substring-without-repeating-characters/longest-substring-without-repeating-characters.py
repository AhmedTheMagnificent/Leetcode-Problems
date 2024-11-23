class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        length = 0
        string = ''
        i = 0
        while i < len(s):
            if s[i] not in string:
                string += s[i]
                length += 1
                i += 1
            else:
                length = 0
                i = i - len(string)
                string = ''
                i += 1
            maxlength = max(maxlength, length)
        return maxlength