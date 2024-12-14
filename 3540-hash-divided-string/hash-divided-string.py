class Solution:
    def stringHash(self, s: str, k: int) -> str:
        strings = []
        result = ""
        j = 0
        n = len(s)
        for i in range(0+k, n, k):
            strings.append(s[j:i])
            j = i
        strings.append(s[j:])
        string = "abcdefghijklmnopqrstuvwxyz"
        values = {s : i for i, s in enumerate(string)}
        keys = {value : key for key, value in values.items()}
        for substr in strings:
            hashedChar = 0
            for i in substr:
                hashedChar += values[i]
            hashedChar %= 26
            result += keys[hashedChar]

        return result


