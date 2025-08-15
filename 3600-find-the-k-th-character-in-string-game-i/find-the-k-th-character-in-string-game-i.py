class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        def wordd(word):
            s = ""
            for w in word:
                s += chr(ord(w) + 1)
            return s
        while len(word) < k:
            word += wordd(word)
        return word[k - 1]

