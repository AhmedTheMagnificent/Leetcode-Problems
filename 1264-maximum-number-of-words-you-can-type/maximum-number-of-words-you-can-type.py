class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        count = 0
        inc = False
        for word in words:
            if list(set(word) & set(brokenLetters)):
                count += 1
        return len(words) - count