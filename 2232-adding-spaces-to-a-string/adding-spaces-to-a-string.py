class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new = ""
        j = 0
        for i in spaces:
            new += s[j:i] + " "
            j = i
        new += s[j:]
        return new