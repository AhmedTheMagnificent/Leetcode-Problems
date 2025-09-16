class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for i in magazine:
            if i not in mag:
                mag[i] = 0
            mag[i] += 1

        for i in ransomNote:
            if i in mag and mag[i] > 0:
                mag[i] -= 1
                continue
            else:
                return False
        return True