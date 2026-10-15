class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        st = "".join([s.lower() for s in licensePlate if s.isalpha()])
        sd = Counter(st)
        ans = ""
        for word in words:
            w = Counter(word)
            if sd <= w:
                if not ans or len(word) < len(ans):    ans = word
        return ans
        