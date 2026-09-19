class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        output = []
        for word in words:
            for row in keyboard:
                if set(word.lower()) <= row:    output.append(word)
        return output