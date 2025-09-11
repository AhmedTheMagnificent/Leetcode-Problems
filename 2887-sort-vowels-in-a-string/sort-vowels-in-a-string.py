class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        vstr = ""
        for i in s:
            if i in vowels:
                vstr += i
        vstr = sorted(vstr)
        idx = 0
        result = []
        for i in s:
            if i in vowels:
                result.append(vstr[idx])
                idx += 1
            else:
                result.append(i)
        return "".join(result)